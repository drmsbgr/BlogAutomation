from PySide6.QtWidgets import *
from model.ui_registerPanel import *
import helper.dbhelper as dbhelper


class RegisterPanel(QMainWindow):
    def __init__(self):
        super(RegisterPanel, self).__init__()

        self.ui = Ui_registerPanel()
        self.ui.setupUi(self)

        self.ui.genderComboBox.clear()
        try:
            con = dbhelper.connectDB()
            cur = con.cursor()
            sql = """SELECT * FROM genders"""
            l = cur.execute(sql, ()).fetchall()
            self.ui.genderComboBox.addItems([row[1] for row in l])
        except Exception as e:
            raise e
        finally:
            con.close()

        self.ui.registerButton.clicked.connect(self.register)
        self.ui.backButton.clicked.connect(self.back)

    def register(self):
        if self.ui.usernameInput.text() == "" or self.ui.passwordInput.text == "":
            QMessageBox.warning(
                self, "Uyarı!", "Boş alan bırakmayınız.", QMessageBox.StandardButton.Ok
            )
            return

        try:
            con = dbhelper.connectDB()
            cur = con.cursor()
            sql = """INSERT INTO accounts VALUES (NULL,?,?,?,?,?,?)"""
            date = self.ui.birthDateInput.date()
            dateStr = f"{date.day()}.{date.month()}.{date.year()}"
            DEFAULT_ROLE_ID = 2
            cur.execute(
                sql,
                (
                    self.ui.usernameInput.text(),
                    self.ui.passwordInput.text(),
                    self.ui.mailInput.text(),
                    self.ui.genderComboBox.currentIndex() + 1,
                    dateStr,
                    DEFAULT_ROLE_ID,
                ),
            )
            con.commit()

            QMessageBox.information(
                self,
                "Bilgi!",
                "Başarılı bir şekilde kayıt oldunuz.",
                QMessageBox.StandardButton.Ok,
            )

            self.openHomepage()

        except Exception as e:
            QMessageBox.critical(
                self, "Hata!", "Bir hata oluştu.", QMessageBox.StandardButton.Ok
            )
            raise e
        finally:
            con.close()

    def openHomepage(self):
        import view.homepagePanel as hp

        self.homepagePanel = hp.HomepagePanel()
        self.homepagePanel.show()
        self.close()

    def back(self):
        import view.loginPanel as lp

        self.close()
        self.loginPanel = lp.LoginPanel()
        self.loginPanel.show()
