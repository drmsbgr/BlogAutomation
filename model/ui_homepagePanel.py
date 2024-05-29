# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'homepagePanel.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_homepagePanel(object):
    def setupUi(self, homepagePanel):
        if not homepagePanel.objectName():
            homepagePanel.setObjectName(u"homepagePanel")
        homepagePanel.resize(1024, 768)
        homepagePanel.setMinimumSize(QSize(1024, 768))
        homepagePanel.setMaximumSize(QSize(1024, 768))
        self.scrollArea = QScrollArea(homepagePanel)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(10, 130, 1001, 541))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 982, 539))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy1)
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.postFrame = QFrame(self.scrollAreaWidgetContents)
        self.postFrame.setObjectName(u"postFrame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.postFrame.sizePolicy().hasHeightForWidth())
        self.postFrame.setSizePolicy(sizePolicy2)
        self.postFrame.setMinimumSize(QSize(0, 300))
        self.postFrame.setFrameShape(QFrame.StyledPanel)
        self.postFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.postFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.titleLabel = QLabel(self.postFrame)
        self.titleLabel.setObjectName(u"titleLabel")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.titleLabel.sizePolicy().hasHeightForWidth())
        self.titleLabel.setSizePolicy(sizePolicy3)
        self.titleLabel.setMinimumSize(QSize(0, 40))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.titleLabel.setFont(font)

        self.verticalLayout_2.addWidget(self.titleLabel)

        self.contentLabel = QLabel(self.postFrame)
        self.contentLabel.setObjectName(u"contentLabel")
        sizePolicy2.setHeightForWidth(self.contentLabel.sizePolicy().hasHeightForWidth())
        self.contentLabel.setSizePolicy(sizePolicy2)
        self.contentLabel.setMinimumSize(QSize(0, 100))
        font1 = QFont()
        font1.setPointSize(10)
        self.contentLabel.setFont(font1)
        self.contentLabel.setAlignment(Qt.AlignJustify|Qt.AlignTop)

        self.verticalLayout_2.addWidget(self.contentLabel)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.ownerLabel = QLabel(self.postFrame)
        self.ownerLabel.setObjectName(u"ownerLabel")

        self.horizontalLayout_2.addWidget(self.ownerLabel)

        self.publishDateLabel = QLabel(self.postFrame)
        self.publishDateLabel.setObjectName(u"publishDateLabel")

        self.horizontalLayout_2.addWidget(self.publishDateLabel)

        self.readMoreBtn = QPushButton(self.postFrame)
        self.readMoreBtn.setObjectName(u"readMoreBtn")
        self.readMoreBtn.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_2.addWidget(self.readMoreBtn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addWidget(self.postFrame)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget = QWidget(homepagePanel)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 689, 1001, 71))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(15, 15, 15, 15)
        self.refreshButton = QPushButton(self.horizontalLayoutWidget)
        self.refreshButton.setObjectName(u"refreshButton")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.refreshButton.sizePolicy().hasHeightForWidth())
        self.refreshButton.setSizePolicy(sizePolicy4)
        self.refreshButton.setMinimumSize(QSize(0, 40))

        self.horizontalLayout.addWidget(self.refreshButton)

        self.adminPanelBtn = QPushButton(self.horizontalLayoutWidget)
        self.adminPanelBtn.setObjectName(u"adminPanelBtn")
        sizePolicy4.setHeightForWidth(self.adminPanelBtn.sizePolicy().hasHeightForWidth())
        self.adminPanelBtn.setSizePolicy(sizePolicy4)
        self.adminPanelBtn.setMinimumSize(QSize(0, 40))

        self.horizontalLayout.addWidget(self.adminPanelBtn)

        self.profileButton = QPushButton(self.horizontalLayoutWidget)
        self.profileButton.setObjectName(u"profileButton")
        sizePolicy4.setHeightForWidth(self.profileButton.sizePolicy().hasHeightForWidth())
        self.profileButton.setSizePolicy(sizePolicy4)
        self.profileButton.setMinimumSize(QSize(0, 40))

        self.horizontalLayout.addWidget(self.profileButton)

        self.logoutButton = QPushButton(self.horizontalLayoutWidget)
        self.logoutButton.setObjectName(u"logoutButton")
        sizePolicy4.setHeightForWidth(self.logoutButton.sizePolicy().hasHeightForWidth())
        self.logoutButton.setSizePolicy(sizePolicy4)
        self.logoutButton.setMinimumSize(QSize(0, 40))

        self.horizontalLayout.addWidget(self.logoutButton)

        self.welcomeLabel = QLabel(homepagePanel)
        self.welcomeLabel.setObjectName(u"welcomeLabel")
        self.welcomeLabel.setGeometry(QRect(10, 10, 1001, 31))
        font2 = QFont()
        font2.setPointSize(12)
        self.welcomeLabel.setFont(font2)
        self.frame = QFrame(homepagePanel)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 50, 1001, 71))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy4.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy4)
        self.label_2.setMinimumSize(QSize(100, 0))
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.searchBarInput = QLineEdit(self.frame)
        self.searchBarInput.setObjectName(u"searchBarInput")
        sizePolicy.setHeightForWidth(self.searchBarInput.sizePolicy().hasHeightForWidth())
        self.searchBarInput.setSizePolicy(sizePolicy)
        self.searchBarInput.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_3.addWidget(self.searchBarInput)

        self.searchBtn = QPushButton(self.frame)
        self.searchBtn.setObjectName(u"searchBtn")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.searchBtn.sizePolicy().hasHeightForWidth())
        self.searchBtn.setSizePolicy(sizePolicy5)
        self.searchBtn.setMinimumSize(QSize(40, 40))
        font3 = QFont()
        font3.setPointSize(8)
        self.searchBtn.setFont(font3)

        self.horizontalLayout_3.addWidget(self.searchBtn)

        self.horizontalSpacer = QSpacerItem(450, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.createPostBtn = QPushButton(self.frame)
        self.createPostBtn.setObjectName(u"createPostBtn")
        sizePolicy5.setHeightForWidth(self.createPostBtn.sizePolicy().hasHeightForWidth())
        self.createPostBtn.setSizePolicy(sizePolicy5)
        self.createPostBtn.setMinimumSize(QSize(150, 40))

        self.horizontalLayout_3.addWidget(self.createPostBtn)


        self.retranslateUi(homepagePanel)

        QMetaObject.connectSlotsByName(homepagePanel)
    # setupUi

    def retranslateUi(self, homepagePanel):
        homepagePanel.setWindowTitle(QCoreApplication.translate("homepagePanel", u"Anasayfa", None))
        self.titleLabel.setText(QCoreApplication.translate("homepagePanel", u"ba\u015fl\u0131k", None))
        self.contentLabel.setText(QCoreApplication.translate("homepagePanel", u"i\u00e7erik", None))
        self.ownerLabel.setText(QCoreApplication.translate("homepagePanel", u"Payla\u015fan:", None))
        self.publishDateLabel.setText(QCoreApplication.translate("homepagePanel", u"Payla\u015f\u0131m Tarihi:", None))
        self.readMoreBtn.setText(QCoreApplication.translate("homepagePanel", u"Devam\u0131n\u0131 oku", None))
        self.refreshButton.setText(QCoreApplication.translate("homepagePanel", u"Yenile", None))
        self.adminPanelBtn.setText(QCoreApplication.translate("homepagePanel", u"Y\u00f6netici Paneli", None))
        self.profileButton.setText(QCoreApplication.translate("homepagePanel", u"Profil", None))
        self.logoutButton.setText(QCoreApplication.translate("homepagePanel", u"\u00c7\u0131k\u0131\u015f Yap", None))
        self.welcomeLabel.setText(QCoreApplication.translate("homepagePanel", u"Ho\u015fgeldiniz ? Bey/Han\u0131m", None))
        self.label_2.setText(QCoreApplication.translate("homepagePanel", u"\u0130\u00e7erik Ara:", None))
        self.searchBtn.setText(QCoreApplication.translate("homepagePanel", u"Ara", None))
        self.createPostBtn.setText(QCoreApplication.translate("homepagePanel", u"G\u00f6nderi Olu\u015ftur", None))
    # retranslateUi

