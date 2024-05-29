from PySide6.QtWidgets import *
from model.ui_homepagePanel import *
from data.account import *
from data.post import *
import helper.dbhelper as dbhelper


class HomepagePanel(QMainWindow):
    def __init__(self, userData: Account):
        super(HomepagePanel, self).__init__()
        self.ui = Ui_homepagePanel()
        self.ui.setupUi(self)
        self.userData = userData

        self.ui.adminPanelBtn.setEnabled(self.userData.roleID == 1)

        self.ui.welcomeLabel.setText(f"Hoşgeldiniz, {self.userData.username}")

        self.ui.searchBarInput.textChanged.connect(self.search)
        self.ui.searchBtn.clicked.connect(self.search)
        self.ui.refreshButton.clicked.connect(lambda: self.refresh(""))
        self.ui.logoutButton.clicked.connect(self.logout)
        self.ui.profileButton.clicked.connect(self.openProfile)
        self.ui.adminPanelBtn.clicked.connect(self.openAdminPanel)
        self.ui.createPostBtn.clicked.connect(self.openCreatePostPanel)

        self.ui.postFrame.hide()
        self.refresh("")

    def search(self):
        self.refresh(self.ui.searchBarInput.text())

    def refresh(self, search):

        for i in reversed(range(self.ui.scrollAreaWidgetContents.layout().count())):
            self.ui.scrollAreaWidgetContents.layout().itemAt(i).widget().setParent(None)

        try:
            con = dbhelper.connectDB()
            cur = con.cursor()
            sql = f"""SELECT post_ID,post_HEADER,post_CONTENT,post_DATE,post_OWNER_ID,account_USERNAME FROM posts
            INNER JOIN accounts ON posts.post_OWNER_ID=accounts.account_ID"""
            if search != "":
                sql += f"""\nWHERE post_HEADER LIKE '%{search}%' OR post_CONTENT LIKE '%{search}%'"""

            sql += """\nORDER BY post_DATE DESC"""

            l = cur.execute(sql, ()).fetchall()

            for row in l:

                postData = Post(row[0], row[1], row[2], row[3], row[4])

                frame = QFrame(self.ui.scrollAreaWidgetContents)
                frame.setFixedHeight(300)
                frame.layout = QVBoxLayout(frame)
                z = frame.sizePolicy()
                z.setVerticalPolicy(QSizePolicy.Policy.Fixed)
                frame.setSizePolicy(z)

                titleLabel = QLabel(frame)
                szplcy = titleLabel.sizePolicy()
                szplcy.setVerticalPolicy(QSizePolicy.Policy.Minimum)
                titleLabel.setSizePolicy(szplcy)
                titleLabel.setMinimumHeight(40)
                font = titleLabel.font()
                font.setBold(True)
                titleLabel.setFont(font)

                contentLabel = QLabel(frame)
                titleLabel.setSizePolicy(szplcy)
                contentLabel.setMinimumHeight(100)
                contentLabel.setWordWrap(True)

                frame2 = QFrame(frame)
                publisherLabel = QLabel(f"Paylaşan: {row[5]}", frame2)
                publishDateLabel = QLabel(f"Paylaşım Tarihi: {postData.date}", frame2)
                readMoreBtn = QPushButton("Devamını oku", frame2)
                readMoreBtn.clicked.connect(
                    lambda clicked, pd=postData: self.readMore(pd, self.userData)
                )

                frame2.setLayout(QHBoxLayout(frame2))
                frame2.layout().addWidget(publisherLabel)
                frame2.layout().addWidget(publishDateLabel)
                frame2.layout().addWidget(readMoreBtn)

                frame.layout.addWidget(titleLabel)
                frame.layout.addWidget(contentLabel)
                frame.layout.addWidget(frame2)

                titleLabel.setText(postData.title)
                contentLabel.setText(
                    str(postData.content)[: int(len(row[2]) * 0.2)] + "..."
                )

                self.ui.scrollAreaWidgetContents.layout().addWidget(frame)

        except Exception as e:
            raise e
        finally:
            con.close()

    def readMore(self, postData: Post, userData: Account):
        import view.postViewPanel as pvp

        self.postViewPanel = pvp.PostViewPanel(postData, userData)
        self.postViewPanel.show()
        self.close()

    def openCreatePostPanel(self):
        import view.createPostPanel as cpp
        
        self.createPostPanel = cpp.CreatePostPanel(self.userData)
        self.createPostPanel.show()
        self.close()

    def openAdminPanel(self):
        import view.adminPanel as ap

        self.adminPanel = ap.AdminPanel(self.userData)
        self.adminPanel.show()
        self.close()

    def logout(self):

        res = QMessageBox.question(
            self,
            "Soru",
            "Çıkış yapmak istediğinize emin misiniz?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No,
        )

        if res == QMessageBox.StandardButton.No:
            return

        import view.loginPanel as lp

        self.loginPanel = lp.LoginPanel()
        self.loginPanel.show()
        self.close()

    def openProfile(self):
        import view.profilePanel as pp

        self.profile = pp.ProfilePanel(self.userData)
        self.profile.show()
        self.close()
