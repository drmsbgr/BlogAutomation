from PySide6.QtWidgets import *
from model.ui_createPostPanel import *
from data.account import *
from data.category import *
import helper.dbhelper as dbhelper


class CreatePostPanel(QMainWindow):
    def __init__(self, userData: Account):
        super(CreatePostPanel, self).__init__()
        self.ui = Ui_createPostPanel()
        self.ui.setupUi(self)
        self.userData = userData

        self.selectedCategories = []
        self.loadCategories()

        self.ui.sendRightBtn.clicked.connect(self.sendRight)
        self.ui.sendLeftBtn.clicked.connect(self.sendLeft)
        self.ui.createBtn.clicked.connect(self.createPost)
        self.ui.backBtn.clicked.connect(self.back)

    def sendRight(self):
        index = self.ui.allCategories.currentIndex().row()

        if index < 0:
            return

        selectedCategory = self.categories[index]

        if selectedCategory not in self.selectedCategories:
            self.selectedCategories.append(selectedCategory)
            self.ui.selectedCategories.addItem(selectedCategory.name)

    def sendLeft(self):
        index = self.ui.selectedCategories.currentIndex().row()

        if index < 0:
            return

        selectedCategory = self.selectedCategories[index]

        self.selectedCategories.remove(selectedCategory)
        self.ui.selectedCategories.takeItem(index)

    def createPost(self):
        if self.ui.titleInput.text() == "" or self.ui.contentInput.toPlainText() == "":
            QMessageBox.warning(
                self, "Uyarı!", "Boş alan bırakmayınız.", QMessageBox.StandardButton.Ok
            )

        try:
            con = dbhelper.connectDB()
            cur = con.cursor()
            sql = """INSERT INTO posts VALUES(NULL,?,?,?,?)"""
            datetime = QDateTime.currentDateTime()
            dateStr = f"{datetime.date().day():02d}.{datetime.date().month():02d}.{datetime.date().year()} {datetime.time().hour():02d}:{datetime.time().minute():02d}:{datetime.time().second():02d}"
            cur.execute(
                sql,
                (
                    self.ui.titleInput.text(),
                    self.ui.contentInput.toPlainText(),
                    dateStr,
                    self.userData.id,
                ),
            )
            con.commit()

            sql2 = """SELECT * FROM posts ORDER BY post_DATE DESC"""
            l = cur.execute(sql2, ()).fetchone()

            sql3 = """INSERT INTO postCategories VALUES(NULL,?,?)"""
            for item in self.selectedCategories:
                cur.execute(sql3, (l[0], item.id))

            con.commit()
            self.back()

        except Exception as e:
            raise e
        finally:
            con.close()

    def loadCategories(self):
        try:
            con = dbhelper.connectDB()
            cur = con.cursor()

            sql = """SELECT * FROM categories"""

            l = cur.execute(sql, ()).fetchall()

            self.categories = [Category(row[0], row[1]) for row in l]

            self.ui.allCategories.clear()
            self.ui.allCategories.addItems([item.name for item in self.categories])

        except Exception as e:
            raise e

        finally:
            con.close()

    def createBtn(self):
        if self.ui.titleInput.text() == "" or self.ui.contentInput.toPlainText() == "":
            QMessageBox.warning(
                self,
                "Uyarı!",
                "Boş alan bırakmayınız...",
                QMessageBox.StandardButton.Ok,
            )
            return

    def back(self):
        import view.homepagePanel as hp

        self.homepagePanel = hp.HomepagePanel(self.userData)
        self.homepagePanel.show()
        self.close()
