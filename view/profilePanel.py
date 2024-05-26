from PySide6.QtWidgets import *
from model.ui_profilePanel import *
from data.account import *
from data.gender import *
import helper.dbhelper as dbhelper


class ProfilePanel(QMainWindow):
    def __init__(self, userData: Account):
        super(ProfilePanel, self).__init__()
        self.ui = Ui_profilePanel()
        self.ui.setupUi(self)
        self.userData = userData

        self.editMode = False

        try:
            self.ui.genderComboBox.clear()

            con = dbhelper.connectDB()
            cur = con.cursor()
            sql = """SELECT * FROM genders"""

            l = cur.execute(sql, ()).fetchall()
            self.genders = [Gender(row[0], row[1]) for row in l]
            self.ui.genderComboBox.addItems([item.name for item in self.genders])

            sql = """SELECT * FROM roles WHERE role_ID=?"""
            row = cur.execute(sql, (self.userData.roleID,)).fetchone()
        except Exception as e:
            raise e
        finally:
            con.close()

        self.ui.usernameInput.setText(self.userData.username)
        self.ui.passwordInput.setText(self.userData.password)
        self.ui.emailInput.setText(self.userData.email)

        for i, item in enumerate(self.genders):
            if item.id == self.userData.genderID:
                self.ui.genderComboBox.setCurrentIndex(i)
                break
        d, m, y = self.userData.birthDate.split(".")
        self.ui.birthDateInput.setDate(QDate(int(y), int(m), int(d)))
        self.ui.roleLabel.setText(f"Rol: {row[1]}")

        self.ui.editOrSaveBtn.clicked.connect(self.editOrSave)
        self.ui.backButton.clicked.connect(self.back)

    def editOrSave(self):
        self.editMode = not self.editMode

        self.ui.usernameInput.setEnabled(self.editMode)
        self.ui.passwordInput.setEnabled(self.editMode)
        self.ui.emailInput.setEnabled(self.editMode)
        self.ui.genderComboBox.setEnabled(self.editMode)
        self.ui.birthDateInput.setEnabled(self.editMode)

        self.ui.editOrSaveBtn.setText("Kaydet" if self.editMode else "Düzenle")
        
        if not self.editMode:
            try:
                con = dbhelper.connectDB()
                cur = con.cursor()
                sql = """UPDATE accounts 
                SET account_USERNAME=?,account_PASSWORD=?,account_MAIL=?,account_GENDER_ID=?,
                account_BIRTHDATE=? 
                WHERE account_ID=?"""

                date = self.ui.birthDateInput.date()
                dateStr = f"{date.day()}.{date.month()}.{date.year()}"

                self.userData.username = self.ui.usernameInput.text()
                self.userData.password = self.ui.passwordInput.text()
                self.userData.email = self.ui.emailInput.text()
                self.userData.genderID = self.genders[
                    self.ui.genderComboBox.currentIndex()
                ].id
                self.userData.birthDate = dateStr

                cur.execute(
                    sql,
                    (
                        self.userData.username,
                        self.userData.password,
                        self.userData.email,
                        self.userData.genderID,
                        self.userData.birthDate,
                        self.userData.id,
                    ),
                )
                con.commit()
            except Exception as e:
                raise e
            finally:
                con.close()

    def back(self):
        import view.homepagePanel as hp

        self.homepagePanel = hp.HomepagePanel(self.userData)
        self.homepagePanel.show()
        self.close()
