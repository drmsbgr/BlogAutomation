# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'createPostPanel.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QPlainTextEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_createPostPanel(object):
    def setupUi(self, createPostPanel):
        if not createPostPanel.objectName():
            createPostPanel.setObjectName(u"createPostPanel")
        createPostPanel.resize(600, 800)
        self.verticalLayoutWidget = QWidget(createPostPanel)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 581, 711))
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
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.frame = QFrame(self.verticalLayoutWidget)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(0, 125))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(0, 30))

        self.verticalLayout_2.addWidget(self.label_2)

        self.titleInput = QLineEdit(self.frame)
        self.titleInput.setObjectName(u"titleInput")
        self.titleInput.setMinimumSize(QSize(0, 30))

        self.verticalLayout_2.addWidget(self.titleInput)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.verticalLayoutWidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QSize(0, 150))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QSize(0, 30))

        self.verticalLayout_3.addWidget(self.label_3)

        self.contentInput = QPlainTextEdit(self.frame_2)
        self.contentInput.setObjectName(u"contentInput")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.contentInput.sizePolicy().hasHeightForWidth())
        self.contentInput.setSizePolicy(sizePolicy1)
        self.contentInput.setMinimumSize(QSize(0, 150))

        self.verticalLayout_3.addWidget(self.contentInput)


        self.verticalLayout.addWidget(self.frame_2)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QSize(0, 30))

        self.verticalLayout.addWidget(self.label_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(15, 15, 15, 15)
        self.allCategories = QListWidget(self.verticalLayoutWidget)
        self.allCategories.setObjectName(u"allCategories")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.allCategories.sizePolicy().hasHeightForWidth())
        self.allCategories.setSizePolicy(sizePolicy2)
        self.allCategories.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_2.addWidget(self.allCategories)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(15, 15, 15, 15)
        self.sendRightBtn = QPushButton(self.verticalLayoutWidget)
        self.sendRightBtn.setObjectName(u"sendRightBtn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.sendRightBtn.sizePolicy().hasHeightForWidth())
        self.sendRightBtn.setSizePolicy(sizePolicy3)

        self.verticalLayout_4.addWidget(self.sendRightBtn)

        self.sendLeftBtn = QPushButton(self.verticalLayoutWidget)
        self.sendLeftBtn.setObjectName(u"sendLeftBtn")
        sizePolicy3.setHeightForWidth(self.sendLeftBtn.sizePolicy().hasHeightForWidth())
        self.sendLeftBtn.setSizePolicy(sizePolicy3)

        self.verticalLayout_4.addWidget(self.sendLeftBtn)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.selectedCategories = QListWidget(self.verticalLayoutWidget)
        self.selectedCategories.setObjectName(u"selectedCategories")
        sizePolicy2.setHeightForWidth(self.selectedCategories.sizePolicy().hasHeightForWidth())
        self.selectedCategories.setSizePolicy(sizePolicy2)
        self.selectedCategories.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_2.addWidget(self.selectedCategories)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayoutWidget = QWidget(createPostPanel)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 730, 581, 61))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(15, 15, 15, 15)
        self.createBtn = QPushButton(self.horizontalLayoutWidget)
        self.createBtn.setObjectName(u"createBtn")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.createBtn.sizePolicy().hasHeightForWidth())
        self.createBtn.setSizePolicy(sizePolicy4)

        self.horizontalLayout.addWidget(self.createBtn)

        self.backBtn = QPushButton(self.horizontalLayoutWidget)
        self.backBtn.setObjectName(u"backBtn")
        sizePolicy4.setHeightForWidth(self.backBtn.sizePolicy().hasHeightForWidth())
        self.backBtn.setSizePolicy(sizePolicy4)

        self.horizontalLayout.addWidget(self.backBtn)


        self.retranslateUi(createPostPanel)

        QMetaObject.connectSlotsByName(createPostPanel)
    # setupUi

    def retranslateUi(self, createPostPanel):
        createPostPanel.setWindowTitle(QCoreApplication.translate("createPostPanel", u"G\u00f6nderi Olu\u015ftur", None))
        self.label.setText(QCoreApplication.translate("createPostPanel", u"G\u00f6nderi Olu\u015ftur", None))
        self.label_2.setText(QCoreApplication.translate("createPostPanel", u"G\u00f6nderi Ba\u015fl\u0131\u011f\u0131", None))
        self.label_3.setText(QCoreApplication.translate("createPostPanel", u"G\u00f6nderi \u0130\u00e7eri\u011fi", None))
        self.label_4.setText(QCoreApplication.translate("createPostPanel", u"Kategoriler", None))
        self.sendRightBtn.setText(QCoreApplication.translate("createPostPanel", u">", None))
        self.sendLeftBtn.setText(QCoreApplication.translate("createPostPanel", u"<", None))
        self.createBtn.setText(QCoreApplication.translate("createPostPanel", u"Olu\u015ftur", None))
        self.backBtn.setText(QCoreApplication.translate("createPostPanel", u"Geri D\u00f6n", None))
    # retranslateUi

