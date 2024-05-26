from PySide6.QtWidgets import *
from view.loginPanel import *
import helper.dbhelper as dbhelper

if __name__ == "__main__":
    import sys

    dbhelper.initializeDB()

    app = QApplication(sys.argv)
    window = LoginPanel()
    window.show()

    sys.exit(app.exec())
