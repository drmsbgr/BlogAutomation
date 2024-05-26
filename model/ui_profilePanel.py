# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'profilePanel.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_profilePanel(object):
    def setupUi(self, profilePanel):
        if not profilePanel.objectName():
            profilePanel.setObjectName(u"profilePanel")
        profilePanel.resize(400, 550)
        profilePanel.setMinimumSize(QSize(400, 550))
        profilePanel.setMaximumSize(QSize(400, 550))
        profilePanel.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayoutWidget = QWidget(profilePanel)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(9, 11, 381, 531))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label)

        self.usernameInput = QLineEdit(self.verticalLayoutWidget)
        self.usernameInput.setObjectName(u"usernameInput")
        self.usernameInput.setEnabled(False)
        self.usernameInput.setMinimumSize(QSize(0, 30))

        self.verticalLayout.addWidget(self.usernameInput)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.label_2)

        self.passwordInput = QLineEdit(self.verticalLayoutWidget)
        self.passwordInput.setObjectName(u"passwordInput")
        self.passwordInput.setEnabled(False)
        self.passwordInput.setMinimumSize(QSize(0, 30))
        self.passwordInput.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.passwordInput)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.label_3)

        self.emailInput = QLineEdit(self.verticalLayoutWidget)
        self.emailInput.setObjectName(u"emailInput")
        self.emailInput.setEnabled(False)
        self.emailInput.setMinimumSize(QSize(0, 30))

        self.verticalLayout.addWidget(self.emailInput)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.label_4)

        self.genderComboBox = QComboBox(self.verticalLayoutWidget)
        self.genderComboBox.setObjectName(u"genderComboBox")
        self.genderComboBox.setEnabled(False)
        self.genderComboBox.setMinimumSize(QSize(0, 30))

        self.verticalLayout.addWidget(self.genderComboBox)

        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.label_5)

        self.birthDateInput = QDateEdit(self.verticalLayoutWidget)
        self.birthDateInput.setObjectName(u"birthDateInput")
        self.birthDateInput.setEnabled(False)
        self.birthDateInput.setMinimumSize(QSize(0, 30))

        self.verticalLayout.addWidget(self.birthDateInput)

        self.roleLabel = QLabel(self.verticalLayoutWidget)
        self.roleLabel.setObjectName(u"roleLabel")
        self.roleLabel.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.roleLabel.sizePolicy().hasHeightForWidth())
        self.roleLabel.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.roleLabel)

        self.editOrSaveBtn = QPushButton(self.verticalLayoutWidget)
        self.editOrSaveBtn.setObjectName(u"editOrSaveBtn")
        self.editOrSaveBtn.setMinimumSize(QSize(0, 30))

        self.verticalLayout.addWidget(self.editOrSaveBtn)

        self.backButton = QPushButton(self.verticalLayoutWidget)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setMinimumSize(QSize(0, 30))
        self.backButton.setLayoutDirection(Qt.LeftToRight)
        self.backButton.setAutoFillBackground(False)

        self.verticalLayout.addWidget(self.backButton)


        self.retranslateUi(profilePanel)

        QMetaObject.connectSlotsByName(profilePanel)
    # setupUi

    def retranslateUi(self, profilePanel):
        profilePanel.setWindowTitle(QCoreApplication.translate("profilePanel", u"Profil", None))
        self.label.setText(QCoreApplication.translate("profilePanel", u"Kullan\u0131c\u0131 Ad\u0131", None))
        self.label_2.setText(QCoreApplication.translate("profilePanel", u"\u015eifre", None))
        self.label_3.setText(QCoreApplication.translate("profilePanel", u"E-Mail", None))
        self.label_4.setText(QCoreApplication.translate("profilePanel", u"Cinsiyet", None))
        self.label_5.setText(QCoreApplication.translate("profilePanel", u"Do\u011fum Tarihi", None))
        self.roleLabel.setText(QCoreApplication.translate("profilePanel", u"Rol: ", None))
        self.editOrSaveBtn.setText(QCoreApplication.translate("profilePanel", u"D\u00fczenle", None))
        self.backButton.setText(QCoreApplication.translate("profilePanel", u"Geri D\u00f6n", None))
    # retranslateUi

