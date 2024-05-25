from PySide6.QtWidgets import *
from model.ui_loginPanel import *

class LoginPanel(QMainWindow):
    def __init__(self):
        super(LoginPanel, self).__init__()
        
        self.ui = Ui_loginPanel()
        self.ui.setupUi(self)