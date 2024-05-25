# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginPanel.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLayout, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_loginPanel(object):
    def setupUi(self, loginPanel):
        if not loginPanel.objectName():
            loginPanel.setObjectName(u"loginPanel")
        loginPanel.resize(400, 350)
        self.verticalLayoutWidget = QWidget(loginPanel)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 381, 331))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.usernameInput = QLineEdit(self.verticalLayoutWidget)
        self.usernameInput.setObjectName(u"usernameInput")
        self.usernameInput.setMinimumSize(QSize(0, 40))

        self.verticalLayout.addWidget(self.usernameInput)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.passwordInput = QLineEdit(self.verticalLayoutWidget)
        self.passwordInput.setObjectName(u"passwordInput")
        self.passwordInput.setMinimumSize(QSize(0, 40))
        self.passwordInput.setMaxLength(32767)
        self.passwordInput.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.passwordInput)

        self.loginButton = QPushButton(self.verticalLayoutWidget)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setMinimumSize(QSize(0, 40))

        self.verticalLayout.addWidget(self.loginButton)

        self.registerButton = QPushButton(self.verticalLayoutWidget)
        self.registerButton.setObjectName(u"registerButton")
        self.registerButton.setMinimumSize(QSize(0, 40))

        self.verticalLayout.addWidget(self.registerButton)


        self.retranslateUi(loginPanel)

        QMetaObject.connectSlotsByName(loginPanel)
    # setupUi

    def retranslateUi(self, loginPanel):
        loginPanel.setWindowTitle(QCoreApplication.translate("loginPanel", u"Giri\u015f Yap", None))
        self.label.setText(QCoreApplication.translate("loginPanel", u"Kullan\u0131c\u0131 Ad\u0131", None))
        self.usernameInput.setPlaceholderText(QCoreApplication.translate("loginPanel", u"Kullan\u0131c\u0131 ad\u0131n\u0131z\u0131 giriniz...", None))
        self.label_2.setText(QCoreApplication.translate("loginPanel", u"\u015eifre", None))
        self.passwordInput.setInputMask("")
        self.passwordInput.setText("")
        self.passwordInput.setPlaceholderText(QCoreApplication.translate("loginPanel", u"\u015eifrenizi giriniz...", None))
        self.loginButton.setText(QCoreApplication.translate("loginPanel", u"Giri\u015f Yap", None))
        self.registerButton.setText(QCoreApplication.translate("loginPanel", u"Hesab\u0131m Yok", None))
    # retranslateUi

