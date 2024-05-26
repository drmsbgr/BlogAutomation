# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'postViewPanel.ui'
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
    QPlainTextEdit, QPushButton, QScrollArea, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_postViewPanel(object):
    def setupUi(self, postViewPanel):
        if not postViewPanel.objectName():
            postViewPanel.setObjectName(u"postViewPanel")
        postViewPanel.resize(675, 900)
        postViewPanel.setMinimumSize(QSize(675, 900))
        postViewPanel.setMaximumSize(QSize(675, 900))
        self.verticalLayoutWidget = QWidget(postViewPanel)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(9, 9, 661, 431))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.frame = QFrame(self.verticalLayoutWidget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(0, 40))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.titleLabel = QLabel(self.frame)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.titleLabel)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.verticalLayoutWidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.contentLabel = QLabel(self.frame_2)
        self.contentLabel.setObjectName(u"contentLabel")
        sizePolicy1.setHeightForWidth(self.contentLabel.sizePolicy().hasHeightForWidth())
        self.contentLabel.setSizePolicy(sizePolicy1)
        self.contentLabel.setScaledContents(True)
        self.contentLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.contentLabel.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.contentLabel)


        self.verticalLayout.addWidget(self.frame_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(15, 15, 15, 15)
        self.publisherLabel = QLabel(self.verticalLayoutWidget)
        self.publisherLabel.setObjectName(u"publisherLabel")
        self.publisherLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.publisherLabel)

        self.publishDateLabel = QLabel(self.verticalLayoutWidget)
        self.publishDateLabel.setObjectName(u"publishDateLabel")
        self.publishDateLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.publishDateLabel)

        self.commentCountLabel = QLabel(self.verticalLayoutWidget)
        self.commentCountLabel.setObjectName(u"commentCountLabel")
        self.commentCountLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.commentCountLabel)

        self.categoriesLabel = QLabel(self.verticalLayoutWidget)
        self.categoriesLabel.setObjectName(u"categoriesLabel")
        self.categoriesLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.categoriesLabel)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.scrollArea = QScrollArea(postViewPanel)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(9, 489, 661, 251))
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 642, 249))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setSpacing(15)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(15, 15, 15, 15)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget_2 = QWidget(postViewPanel)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 750, 661, 101))
        self.horizontalLayout_2 = QHBoxLayout(self.verticalLayoutWidget_2)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(15, 15, 15, 15)
        self.plainTextEdit = QPlainTextEdit(self.verticalLayoutWidget_2)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.horizontalLayout_2.addWidget(self.plainTextEdit)

        self.sendCommentButton = QPushButton(self.verticalLayoutWidget_2)
        self.sendCommentButton.setObjectName(u"sendCommentButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.sendCommentButton.sizePolicy().hasHeightForWidth())
        self.sendCommentButton.setSizePolicy(sizePolicy2)
        self.sendCommentButton.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_2.addWidget(self.sendCommentButton)

        self.label = QLabel(postViewPanel)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 450, 661, 31))
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.backButton = QPushButton(postViewPanel)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setGeometry(QRect(570, 860, 100, 31))
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.backButton.sizePolicy().hasHeightForWidth())
        self.backButton.setSizePolicy(sizePolicy4)
        self.backButton.setMinimumSize(QSize(100, 0))

        self.retranslateUi(postViewPanel)

        QMetaObject.connectSlotsByName(postViewPanel)
    # setupUi

    def retranslateUi(self, postViewPanel):
        postViewPanel.setWindowTitle(QCoreApplication.translate("postViewPanel", u"G\u00f6nderi Ekran\u0131", None))
        self.titleLabel.setText(QCoreApplication.translate("postViewPanel", u"BA\u015eLIK", None))
        self.contentLabel.setText(QCoreApplication.translate("postViewPanel", u"\u0130\u00c7ER\u0130K", None))
        self.publisherLabel.setText(QCoreApplication.translate("postViewPanel", u"Payla\u015fan:", None))
        self.publishDateLabel.setText(QCoreApplication.translate("postViewPanel", u"Payla\u015f\u0131m Tarihi:", None))
        self.commentCountLabel.setText(QCoreApplication.translate("postViewPanel", u"Yorum Say\u0131s\u0131:", None))
        self.categoriesLabel.setText(QCoreApplication.translate("postViewPanel", u"Kategoriler:", None))
        self.sendCommentButton.setText(QCoreApplication.translate("postViewPanel", u"Yorum G\u00f6nder", None))
        self.label.setText(QCoreApplication.translate("postViewPanel", u"Yorumlar", None))
        self.backButton.setText(QCoreApplication.translate("postViewPanel", u"Geri D\u00f6n", None))
    # retranslateUi

