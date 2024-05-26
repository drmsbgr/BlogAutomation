from PySide6.QtWidgets import *
from model.ui_postViewPanel import *
from data.account import *
from data.post import *
import helper.dbhelper as dbhelper


class PostViewPanel(QMainWindow):
    def __init__(self, postData: Post, userData: Account):
        super(PostViewPanel, self).__init__()
        self.ui = Ui_postViewPanel()
        self.ui.setupUi(self)

        self.postData = postData
        self.userData = userData

        self.setWindowTitle(self.postData.title)
        self.ui.titleLabel.setText(self.postData.title)
        self.ui.contentLabel.setText(self.postData.content)

        publisher = dbhelper.getAccountById(self.postData.publisherID)

        self.ui.publisherLabel.setText(f"Paylaşan: {publisher.username}")
        self.ui.publishDateLabel.setText(f"Paylaşım Tarihi: {self.postData.date}")

        comments = dbhelper.getCommentsByPostId(self.postData.id)

        for comment in comments:
            frame = QFrame(self.ui.scrollAreaWidgetContents)
            sp = frame.sizePolicy()
            sp.setVerticalPolicy(QSizePolicy.Policy.Fixed)
            sp.setHorizontalPolicy(QSizePolicy.Policy.Preferred)
            frame.setSizePolicy(sp)
            frame.setFixedHeight(150)
            vLayout = QVBoxLayout(frame)
            label1 = QLabel(dbhelper.getAccountById(comment.ownerID).username)
            sp = label1.sizePolicy()
            sp.setHorizontalPolicy(QSizePolicy.Policy.Preferred)
            font = label1.font()
            font.setBold(True)
            label1.setFont(font)
            label2 = QLabel(comment.content)
            label3 = QLabel(f"Paylaşım Tarihi: {comment.date}")

            label1.setSizePolicy(sp)
            label2.setSizePolicy(sp)
            label3.setSizePolicy(sp)

            frame.setLayout(vLayout)
            vLayout.addWidget(label1)
            vLayout.addWidget(label2)
            vLayout.addWidget(label3)
            self.ui.scrollAreaWidgetContents.layout().addWidget(frame)

        self.ui.commentCountLabel.setText(f"Yorum Sayısı: {len(comments)}")

        categories = dbhelper.getCategoriesByPostId(self.postData.id)
        categoriesStr = ",".join(categories)
        self.ui.categoriesLabel.setText(f"Kategoriler: {categoriesStr}")

        self.ui.backButton.clicked.connect(self.back)

    def back(self):
        import view.homepagePanel as hp

        self.homepagePanel = hp.HomepagePanel(self.userData)
        self.homepagePanel.show()
        self.close()
