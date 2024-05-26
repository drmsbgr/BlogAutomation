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

        self.refreshComments()

        categories = dbhelper.getCategoriesByPostId(self.postData.id)
        categoriesStr = ",".join(categories)
        self.ui.categoriesLabel.setText(f"Kategoriler: {categoriesStr}")

        self.ui.sendCommentButton.clicked.connect(self.sendComment)
        self.ui.backButton.clicked.connect(self.back)

    def refreshComments(self):

        for i in reversed(range(self.ui.scrollAreaWidgetContents.layout().count())):
            self.ui.scrollAreaWidgetContents.layout().itemAt(i).widget().setParent(None)

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

    def sendComment(self):
        if self.ui.commentContentInput.toPlainText() == "":
            QMessageBox.warning(
                self, "Uyarı!", "Boş alan bırakılamaz.", QMessageBox.StandardButton.Ok
            )
            return

        try:
            con = dbhelper.connectDB()
            cur = con.cursor()
            sql = """INSERT INTO comments VALUES (NULL,?,?,?,?)"""
            date = QDateTime.currentDateTime()
            dateStr = f"{date.date().day():02d}.{date.date().month():02d}.{date.date().year():02d} {date.time().hour():02d}:{date.time().minute():02d}:{date.time().second():02d}"
            cur.execute(
                sql,
                (
                    self.userData.id,
                    self.postData.id,
                    self.ui.commentContentInput.toPlainText(),
                    dateStr,
                ),
            )
            con.commit()
            self.refreshComments()
        except Exception as e:
            raise e
        finally:
            con.close()

        self.ui.commentContentInput.setPlainText("")

    def back(self):
        import view.homepagePanel as hp

        self.homepagePanel = hp.HomepagePanel(self.userData)
        self.homepagePanel.show()
        self.close()
