# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'adminPanel.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_adminPanel(object):
    def setupUi(self, adminPanel):
        if not adminPanel.objectName():
            adminPanel.setObjectName(u"adminPanel")
        adminPanel.resize(800, 800)
        self.mainTable = QTableWidget(adminPanel)
        self.mainTable.setObjectName(u"mainTable")
        self.mainTable.setGeometry(QRect(200, 10, 591, 331))
        self.mainTable.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.mainTable.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.mainTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.mainTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.mainTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.mainTable.horizontalHeader().setCascadingSectionResizes(True)
        self.mainTable.horizontalHeader().setProperty("showSortIndicator", True)
        self.mainTable.horizontalHeader().setStretchLastSection(True)
        self.verticalLayoutWidget = QWidget(adminPanel)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 181, 331))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(0, 40))
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.selectPostsBtn = QPushButton(self.verticalLayoutWidget)
        self.selectPostsBtn.setObjectName(u"selectPostsBtn")
        self.selectPostsBtn.setMinimumSize(QSize(0, 40))

        self.verticalLayout.addWidget(self.selectPostsBtn)

        self.selectCategoriesBtn = QPushButton(self.verticalLayoutWidget)
        self.selectCategoriesBtn.setObjectName(u"selectCategoriesBtn")
        self.selectCategoriesBtn.setMinimumSize(QSize(0, 40))

        self.verticalLayout.addWidget(self.selectCategoriesBtn)

        self.selectCommentsBtn = QPushButton(self.verticalLayoutWidget)
        self.selectCommentsBtn.setObjectName(u"selectCommentsBtn")
        self.selectCommentsBtn.setMinimumSize(QSize(0, 40))

        self.verticalLayout.addWidget(self.selectCommentsBtn)

        self.selectAccountsBtn = QPushButton(self.verticalLayoutWidget)
        self.selectAccountsBtn.setObjectName(u"selectAccountsBtn")
        self.selectAccountsBtn.setMinimumSize(QSize(0, 40))

        self.verticalLayout.addWidget(self.selectAccountsBtn)

        self.verticalLayoutWidget_2 = QWidget(adminPanel)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 350, 561, 441))
        self.inputLayout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.inputLayout.setSpacing(5)
        self.inputLayout.setObjectName(u"inputLayout")
        self.inputLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayoutWidget_3 = QWidget(adminPanel)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(580, 350, 211, 441))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(15, 15, 15, 15)
        self.label_2 = QLabel(self.verticalLayoutWidget_3)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(0, 40))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.addNewRecordBtn = QPushButton(self.verticalLayoutWidget_3)
        self.addNewRecordBtn.setObjectName(u"addNewRecordBtn")
        self.addNewRecordBtn.setMinimumSize(QSize(0, 40))

        self.verticalLayout_2.addWidget(self.addNewRecordBtn)

        self.editRecordBtn = QPushButton(self.verticalLayoutWidget_3)
        self.editRecordBtn.setObjectName(u"editRecordBtn")
        self.editRecordBtn.setMinimumSize(QSize(0, 40))

        self.verticalLayout_2.addWidget(self.editRecordBtn)

        self.deleteRecordsBtn = QPushButton(self.verticalLayoutWidget_3)
        self.deleteRecordsBtn.setObjectName(u"deleteRecordsBtn")
        self.deleteRecordsBtn.setMinimumSize(QSize(0, 40))

        self.verticalLayout_2.addWidget(self.deleteRecordsBtn)

        self.backButton = QPushButton(self.verticalLayoutWidget_3)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setMinimumSize(QSize(0, 40))

        self.verticalLayout_2.addWidget(self.backButton)


        self.retranslateUi(adminPanel)

        QMetaObject.connectSlotsByName(adminPanel)
    # setupUi

    def retranslateUi(self, adminPanel):
        adminPanel.setWindowTitle(QCoreApplication.translate("adminPanel", u"Y\u00f6netici Paneli", None))
        self.label.setText(QCoreApplication.translate("adminPanel", u"Tablo Se\u00e7in", None))
        self.selectPostsBtn.setText(QCoreApplication.translate("adminPanel", u"G\u00f6nderiler", None))
        self.selectCategoriesBtn.setText(QCoreApplication.translate("adminPanel", u"Kategoriler", None))
        self.selectCommentsBtn.setText(QCoreApplication.translate("adminPanel", u"Yorumlar", None))
        self.selectAccountsBtn.setText(QCoreApplication.translate("adminPanel", u"Hesaplar", None))
        self.label_2.setText(QCoreApplication.translate("adminPanel", u"\u0130\u015flemler", None))
        self.addNewRecordBtn.setText(QCoreApplication.translate("adminPanel", u"Yeni Kay\u0131t Ekle", None))
        self.editRecordBtn.setText(QCoreApplication.translate("adminPanel", u"Kayd\u0131 D\u00fczenle", None))
        self.deleteRecordsBtn.setText(QCoreApplication.translate("adminPanel", u"Kayd\u0131 Sil", None))
        self.backButton.setText(QCoreApplication.translate("adminPanel", u"Geri D\u00f6n", None))
    # retranslateUi

