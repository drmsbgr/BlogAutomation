from PySide6.QtWidgets import *
from model.ui_loginPanel import *
from data.account import *
import helper.dbhelper as dbhelper


class LoginPanel(QMainWindow):
    def __init__(self):
        super(LoginPanel, self).__init__()

        self.ui = Ui_loginPanel()
        self.ui.setupUi(self)

        self.ui.loginButton.clicked.connect(self.login)
        self.ui.registerButton.clicked.connect(self.register)
        self.ui.quitButton.clicked.connect(self.quit)

    def login(self):
        if self.ui.usernameInput.text() == "" or self.ui.passwordInput.text == "":
            QMessageBox.warning(
                self, "Uyarı!", "Boş alan bırakmayınız.", QMessageBox.StandardButton.Ok
            )
            return
        try:
            con = dbhelper.connectDB()
            cur = con.cursor()

            sql = """SELECT * FROM accounts WHERE account_USERNAME=? AND account_PASSWORD=?"""

            cur.execute(
                sql, (self.ui.usernameInput.text(), self.ui.passwordInput.text())
            )

            row = cur.fetchone()

            if row == None:
                QMessageBox.warning(
                    self,
                    "Uyarı!",
                    "Kullanıcı adınız veya şifreniz yanlış.",
                    QMessageBox.StandardButton.Ok,
                )
                return

            QMessageBox.information(
                self,
                "Bilgi!",
                "Başarılı bir şekilde giriş yaptınız.",
                QMessageBox.StandardButton.Ok,
            )

            self.openHomepage(
                Account(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            )

        except Exception as e:
            raise e
        finally:
            con.close()

    def openHomepage(self, userData: Account):
        import view.homepagePanel as hp

        self.homepagePanel = hp.HomepagePanel(userData)
        self.homepagePanel.show()
        self.close()

    def register(self):
        import view.registerPanel as rp

        self.registerPanel = rp.RegisterPanel()
        self.registerPanel.show()
        self.close()

    def quit(self):
        self.close()
