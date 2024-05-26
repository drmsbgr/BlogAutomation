# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registerPanel.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QLabel,
    QLayout, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_registerPanel(object):
    def setupUi(self, registerPanel):
        if not registerPanel.objectName():
            registerPanel.setObjectName(u"registerPanel")
        registerPanel.resize(400, 600)
        self.verticalLayoutWidget = QWidget(registerPanel)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 381, 581))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMinAndMaxSize)
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

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.mailInput = QLineEdit(self.verticalLayoutWidget)
        self.mailInput.setObjectName(u"mailInput")
        self.mailInput.setMinimumSize(QSize(0, 40))
        self.mailInput.setMaxLength(32767)
        self.mailInput.setEchoMode(QLineEdit.Normal)

        self.verticalLayout.addWidget(self.mailInput)

        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_5)

        self.genderComboBox = QComboBox(self.verticalLayoutWidget)
        self.genderComboBox.addItem("")
        self.genderComboBox.addItem("")
        self.genderComboBox.addItem("")
        self.genderComboBox.setObjectName(u"genderComboBox")
        self.genderComboBox.setMinimumSize(QSize(0, 40))

        self.verticalLayout.addWidget(self.genderComboBox)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_4)

        self.birthDateInput = QDateEdit(self.verticalLayoutWidget)
        self.birthDateInput.setObjectName(u"birthDateInput")
        self.birthDateInput.setMinimumSize(QSize(0, 40))

        self.verticalLayout.addWidget(self.birthDateInput)

        self.registerButton = QPushButton(self.verticalLayoutWidget)
        self.registerButton.setObjectName(u"registerButton")
        self.registerButton.setMinimumSize(QSize(0, 40))

        self.verticalLayout.addWidget(self.registerButton)

        self.backButton = QPushButton(self.verticalLayoutWidget)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setMinimumSize(QSize(0, 40))

        self.verticalLayout.addWidget(self.backButton)


        self.retranslateUi(registerPanel)

        QMetaObject.connectSlotsByName(registerPanel)
    # setupUi

    def retranslateUi(self, registerPanel):
        registerPanel.setWindowTitle(QCoreApplication.translate("registerPanel", u"Kay\u0131t Ol", None))
        self.label.setText(QCoreApplication.translate("registerPanel", u"Kullan\u0131c\u0131 Ad\u0131", None))
        self.usernameInput.setPlaceholderText(QCoreApplication.translate("registerPanel", u"Kullan\u0131c\u0131 ad\u0131n\u0131z\u0131 giriniz...", None))
        self.label_2.setText(QCoreApplication.translate("registerPanel", u"\u015eifre", None))
        self.passwordInput.setInputMask("")
        self.passwordInput.setText("")
        self.passwordInput.setPlaceholderText(QCoreApplication.translate("registerPanel", u"\u015eifrenizi giriniz...", None))
        self.label_3.setText(QCoreApplication.translate("registerPanel", u"E-Mail", None))
        self.mailInput.setInputMask("")
        self.mailInput.setText("")
        self.mailInput.setPlaceholderText(QCoreApplication.translate("registerPanel", u"E-mailinizi giriniz...", None))
        self.label_5.setText(QCoreApplication.translate("registerPanel", u"Cinsiyet", None))
        self.genderComboBox.setItemText(0, QCoreApplication.translate("registerPanel", u"Erkek", None))
        self.genderComboBox.setItemText(1, QCoreApplication.translate("registerPanel", u"Kad\u0131n", None))
        self.genderComboBox.setItemText(2, QCoreApplication.translate("registerPanel", u"Belirtmek \u0130stemiyorum", None))

        self.label_4.setText(QCoreApplication.translate("registerPanel", u"Do\u011fum Tarihi", None))
        self.registerButton.setText(QCoreApplication.translate("registerPanel", u"Kay\u0131t Ol", None))
        self.backButton.setText(QCoreApplication.translate("registerPanel", u"Geri D\u00f6n", None))
    # retranslateUi

