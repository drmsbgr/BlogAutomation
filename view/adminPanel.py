from PySide6.QtWidgets import *
from PySide6.QtCore import *
from model.ui_adminPanel import *
from data.account import *
from data.category import *
import helper.dbhelper as dbhelper


class AdminPanel(QMainWindow):
    def __init__(self, userData: Account):
        super(AdminPanel, self).__init__()
        self.ui = Ui_adminPanel()
        self.ui.setupUi(self)
        self.userData = userData

        self.ui.selectAccountsBtn.clicked.connect(self.selectAccountsTable)
        self.ui.selectCategoriesBtn.clicked.connect(self.selectCategoriesTable)
        self.ui.selectCommentsBtn.clicked.connect(self.selectCommentsTable)
        self.ui.selectPostsBtn.clicked.connect(self.selectPostsTable)
        self.ui.backButton.clicked.connect(self.back)

        self.ui.mainTable.currentItemChanged.connect(self.updateInputs)
        self.ui.addNewRecordBtn.clicked.connect(self.addRecord)
        self.ui.editRecordBtn.clicked.connect(self.editRecord)
        self.ui.deleteRecordsBtn.clicked.connect(self.deleteRecord)

        self.mode = ""

    def updateInputs(self):
        index = self.ui.mainTable.currentRow()
        if index < 0:
            return

        match self.mode:
            case "accounts":
                self.usernameInput.setText(self.accountTableData[index][1])
                self.passwordInput.setText(self.accountTableData[index][2])
                self.mailInput.setText(self.accountTableData[index][3])

                d, m, y = self.accountTableData[index][4].split(".")

                self.birthDateInput.setDate(QDate(int(y), int(m), int(d)))

                for i, item in enumerate(self.genders):
                    if item[0] == self.accountTableData[index][5]:
                        self.genderInput.setCurrentIndex(i)
                        break

                for i, item in enumerate(self.roles):
                    if item[0] == self.accountTableData[index][7]:
                        self.roleInput.setCurrentIndex(i)
                        break
                pass
            case "posts":
                self.titleInput.setText(self.postsPair[index][0])
                self.contentInput.setPlainText(self.postsPair[index][1])
            case "categories":
                self.categoryNameInput.setText(self.categories[index].name)
            case "comments":
                self.commentContentInput.setPlainText(self.commentsContent[index])

    def addRecord(self):
        match self.mode:
            case "categories":
                if self.categoryNameInput.text() == "":
                    return

                try:
                    con = dbhelper.connectDB()
                    cur = con.cursor()
                    sql = """INSERT INTO categories VALUES(NULL,?)"""
                    cur.execute(sql, (self.categoryNameInput.text(),))
                    con.commit()
                except Exception as e:
                    raise e
                finally:
                    con.close()

                self.selectCategoriesTable()
            case "accounts":
                if (
                    self.usernameInput.text() == ""
                    or self.passwordInput.text() == ""
                    or self.mailInput.text() == ""
                ):
                    return

                try:
                    con = dbhelper.connectDB()
                    cur = con.cursor()
                    sql = """INSERT INTO accounts VALUES(NULL,?,?,?,?,?,?)"""
                    date = self.birthDateInput.date()
                    dateStr = f"{date.day():02d}.{date.month():02d}.{date.year()}"
                    cur.execute(
                        sql,
                        (
                            self.usernameInput.text(),
                            self.passwordInput.text(),
                            self.mailInput.text(),
                            self.genders[self.genderInput.currentIndex()][0],
                            dateStr,
                            self.roles[self.roleInput.currentIndex()][0],
                        ),
                    )
                    con.commit()
                except Exception as e:
                    raise e
                finally:
                    con.close()

                self.selectAccountsTable()

    def editRecord(self):
        index = self.ui.mainTable.currentRow()

        if index < 0:
            return

        match self.mode:
            case "categories":
                if self.categoryNameInput.text() == "":
                    return

                try:
                    con = dbhelper.connectDB()
                    cur = con.cursor()
                    sql = (
                        """UPDATE categories SET category_NAME=? WHERE category_ID=?"""
                    )
                    cur.execute(
                        sql, (self.categoryNameInput.text(), self.categories[index].id)
                    )
                    con.commit()
                except Exception as e:
                    raise e
                finally:
                    con.close()

                self.selectCategoriesTable()
            case "posts":
                if (
                    self.titleInput.text() == ""
                    or self.contentInput.toPlainText() == ""
                ):
                    return
                try:
                    con = dbhelper.connectDB()
                    cur = con.cursor()
                    sql = """UPDATE posts SET post_HEADER=?,post_CONTENT=? WHERE post_ID=?"""
                    cur.execute(
                        sql,
                        (
                            self.titleInput.text(),
                            self.contentInput.toPlainText(),
                            self.posts[index],
                        ),
                    )
                    con.commit()
                except Exception as e:
                    raise e
                finally:
                    con.close()

                self.selectPostsTable()
            case "comments":
                if self.commentContentInput.toPlainText() == "":
                    return

                try:
                    con = dbhelper.connectDB()
                    cur = con.cursor()
                    sql = """UPDATE comments SET comment_CONTENT=? WHERE comment_ID=?"""
                    cur.execute(
                        sql,
                        (self.commentContentInput.toPlainText(), self.comments[index]),
                    )
                    con.commit()
                except Exception as e:
                    raise e
                finally:
                    con.close()

                self.selectCommentsTable()
            case "accounts":
                if (
                    self.usernameInput.text() == ""
                    or self.passwordInput.text() == ""
                    or self.mailInput.text() == ""
                ):
                    return

                try:
                    con = dbhelper.connectDB()
                    cur = con.cursor()
                    sql = """UPDATE accounts SET account_USERNAME=?,account_PASSWORD=?,account_MAIL=?,account_GENDER_ID=?,account_BIRTHDATE=?,account_ROLE_ID=? WHERE account_ID=?"""
                    date = self.birthDateInput.date()
                    dateStr = f"{date.day():02d}.{date.month():02d}.{date.year()}"
                    cur.execute(
                        sql,
                        (
                            self.usernameInput.text(),
                            self.passwordInput.text(),
                            self.mailInput.text(),
                            self.genders[self.genderInput.currentIndex()],
                            dateStr,
                            self.roles[self.roleInput.currentIndex()],
                            self.accountTableData[index][0],
                        ),
                    )
                    con.commit()
                except Exception as e:
                    raise e
                finally:
                    con.close()

                self.selectCommentsTable()

    def deleteRecord(self):
        index = self.ui.mainTable.currentRow()

        if index < 0:
            return

        match self.mode:
            case "accounts":
                try:
                    con = dbhelper.connectDB()
                    cur = con.cursor()
                    sql = """DELETE FROM accounts WHERE account_ID=?"""
                    cur.execute(sql, (self.accountTableData[index][0],))
                    con.commit()
                except Exception as e:
                    raise e
                finally:
                    con.close()

                self.selectAccountsTable()
            case "posts":
                try:
                    con = dbhelper.connectDB()
                    cur = con.cursor()
                    sql = """DELETE FROM posts WHERE post_ID=?"""
                    cur.execute(sql, (self.posts[index],))
                    sql2 = """DELETE FROM postCategories WHERE post_ID=?"""
                    cur.execute(sql2, (self.posts[index],))
                    con.commit()
                except Exception as e:
                    raise e
                finally:
                    con.close()

                self.selectPostsTable()
            case "categories":
                try:
                    con = dbhelper.connectDB()
                    cur = con.cursor()
                    sql = """DELETE FROM categories WHERE category_ID=?"""
                    cur.execute(sql, (self.categories[index].id,))
                    con.commit()
                except Exception as e:
                    raise e
                finally:
                    con.close()

                self.selectCategoriesTable()
            case "comments":
                try:
                    con = dbhelper.connectDB()
                    cur = con.cursor()
                    sql = """DELETE FROM comments WHERE comment_ID=?"""
                    cur.execute(sql, (self.comments[index],))
                    con.commit()
                except Exception as e:
                    raise e
                finally:
                    con.close()

                self.selectCommentsTable()

    def selectCategoriesTable(self):
        self.ui.addNewRecordBtn.setEnabled(True)
        self.mode = "categories"
        self.ui.mainTable.clear()

        for i in reversed(range(self.ui.inputLayout.layout().count())):
            self.ui.inputLayout.layout().itemAt(i).widget().setParent(None)

        self.categoryNameLabel = QLabel("Kategori Adı")
        self.categoryNameInput = QLineEdit("")
        self.categoryNameInput.setPlaceholderText("Kategori adı giriniz...")
        self.ui.inputLayout.layout().addWidget(self.categoryNameLabel)
        self.ui.inputLayout.layout().addWidget(self.categoryNameInput)

        try:
            con = dbhelper.connectDB()
            cur = con.cursor()

            sql = """SELECT * FROM categories"""

            l = cur.execute(sql, ()).fetchall()

            self.categories = [Category(row[0], row[1]) for row in l]

            self.ui.mainTable.setRowCount(len(l))
            self.ui.mainTable.setColumnCount(1)

            self.ui.mainTable.setHorizontalHeaderLabels(["Kategori Adı"])

            for i, row in enumerate(self.categories):
                self.ui.mainTable.setItem(i, 0, QTableWidgetItem(row.name))

        except Exception as e:
            raise e
        finally:
            con.close()

    def selectCommentsTable(self):
        self.ui.addNewRecordBtn.setEnabled(False)
        self.mode = "comments"
        self.ui.mainTable.clear()

        for i in reversed(range(self.ui.inputLayout.layout().count())):
            self.ui.inputLayout.layout().itemAt(i).widget().setParent(None)

        self.commentContentLabel = QLabel("İçerik")
        self.commentContentInput = QPlainTextEdit()

        self.ui.inputLayout.layout().addWidget(self.commentContentLabel)
        self.ui.inputLayout.layout().addWidget(self.commentContentInput)

        try:
            con = dbhelper.connectDB()
            cur = con.cursor()

            sql = """SELECT comment_ID,account_USERNAME,comment_CONTENT,comment_DATE,post_HEADER FROM comments
            INNER JOIN accounts ON comments.comment_OWNER_ID=accounts.account_ID
            INNER JOIN posts ON comments.comment_POST_ID=posts.post_ID
            ORDER BY comment_DATE DESC"""

            l = cur.execute(sql, ()).fetchall()

            self.comments = [item[0] for item in l]
            self.commentsContent = [item[2] for item in l]

            self.ui.mainTable.setRowCount(len(l))
            self.ui.mainTable.setColumnCount(4)

            self.ui.mainTable.setHorizontalHeaderLabels(
                ["Paylaşan", "İçerik", "Tarih", "Gönderi"]
            )

            for i, row in enumerate(l):
                for j, item in enumerate(row[1:]):
                    self.ui.mainTable.setItem(i, j, QTableWidgetItem(item))

        except Exception as e:
            raise e
        finally:
            con.close()

    def selectPostsTable(self):
        self.ui.addNewRecordBtn.setEnabled(False)
        self.mode = "posts"
        self.ui.mainTable.clear()

        for i in reversed(range(self.ui.inputLayout.layout().count())):
            self.ui.inputLayout.layout().itemAt(i).widget().setParent(None)

        self.titleLabel = QLabel("Başlık")
        self.titleInput = QLineEdit()
        self.titleInput.setPlaceholderText("Başlık giriniz...")

        self.contentLabel = QLabel("İçerik")
        self.contentInput = QPlainTextEdit()

        self.ui.inputLayout.layout().addWidget(self.titleLabel)
        self.ui.inputLayout.layout().addWidget(self.titleInput)
        self.ui.inputLayout.layout().addWidget(self.contentLabel)
        self.ui.inputLayout.layout().addWidget(self.contentInput)

        try:
            con = dbhelper.connectDB()
            cur = con.cursor()

            sql = """SELECT post_ID,post_HEADER,post_CONTENT,post_DATE,account_USERNAME FROM posts
            INNER JOIN accounts ON posts.post_OWNER_ID=accounts.account_ID
            ORDER BY post_DATE DESC"""

            l = cur.execute(sql, ()).fetchall()

            self.posts = [row[0] for row in l]
            self.postsPair = [(row[1], row[2]) for row in l]

            self.ui.mainTable.setRowCount(len(l))
            self.ui.mainTable.setColumnCount(4)

            self.ui.mainTable.setHorizontalHeaderLabels(
                ["Başlık", "Gönderi Tarihi", "Paylaşan", "Gönderi Kategorileri"]
            )

            sql2 = """SELECT category_NAME FROM postCategories
            INNER JOIN categories ON postCategories.category_ID=categories.category_ID
            WHERE post_ID=?"""

            for i, row in enumerate(l):
                postCategories = cur.execute(sql2, (row[0],)).fetchall()
                for j, item in enumerate(row[2:]):
                    self.ui.mainTable.setItem(i, j, QTableWidgetItem(item))

                postCategories = [item[0] for item in postCategories]
                self.ui.mainTable.setItem(
                    i, 3, QTableWidgetItem(",".join(postCategories))
                )

        except Exception as e:
            raise e
        finally:
            con.close()

    def selectAccountsTable(self):
        self.ui.addNewRecordBtn.setEnabled(True)
        self.mode = "accounts"
        self.ui.mainTable.clear()

        for i in reversed(range(self.ui.inputLayout.layout().count())):
            self.ui.inputLayout.layout().itemAt(i).widget().setParent(None)

        self.usernameLabel = QLabel("Kullanıcı Adı")
        self.usernameInput = QLineEdit("")
        self.usernameInput.setPlaceholderText("Kullanıcı adı giriniz...")

        self.passwordLabel = QLabel("Şifre")
        self.passwordInput = QLineEdit("")
        self.passwordInput.setPlaceholderText("Şifre giriniz...")
        self.passwordInput.setEchoMode(QLineEdit.EchoMode.Password)

        self.mailLabel = QLabel("Email")
        self.mailInput = QLineEdit("")
        self.mailInput.setPlaceholderText("Email giriniz...")

        self.genderLabel = QLabel("Cinsiyet")
        self.genderInput = QComboBox()

        self.birthDateLabel = QLabel("Doğum Tarihi")
        self.birthDateInput = QDateEdit()

        self.roleLabel = QLabel("Rol")
        self.roleInput = QComboBox()

        self.ui.inputLayout.layout().addWidget(self.usernameLabel)
        self.ui.inputLayout.layout().addWidget(self.usernameInput)
        self.ui.inputLayout.layout().addWidget(self.passwordLabel)
        self.ui.inputLayout.layout().addWidget(self.passwordInput)
        self.ui.inputLayout.layout().addWidget(self.mailLabel)
        self.ui.inputLayout.layout().addWidget(self.mailInput)
        self.ui.inputLayout.layout().addWidget(self.genderLabel)
        self.ui.inputLayout.layout().addWidget(self.genderInput)
        self.ui.inputLayout.layout().addWidget(self.birthDateLabel)
        self.ui.inputLayout.layout().addWidget(self.birthDateInput)
        self.ui.inputLayout.layout().addWidget(self.roleLabel)
        self.ui.inputLayout.layout().addWidget(self.roleInput)

        try:
            con = dbhelper.connectDB()
            cur = con.cursor()

            sql = """SELECT account_ID,account_USERNAME,account_PASSWORD,account_MAIL,account_BIRTHDATE,gender_ID,gender_NAME,role_ID,role_NAME FROM accounts
            INNER JOIN genders ON accounts.account_GENDER_ID=genders.gender_ID
            INNER JOIN roles ON accounts.account_ROLE_ID=roles.role_ID"""

            l = cur.execute(sql, ()).fetchall()

            self.accountTableData = l

            sql2 = """SELECT * FROM genders"""
            self.genders = cur.execute(sql2, ()).fetchall()
            sql3 = """SELECT * FROM roles"""
            self.roles = cur.execute(sql3, ()).fetchall()

            self.genderInput.addItems([row[1] for row in self.genders])
            self.roleInput.addItems([row[1] for row in self.roles])
            self.roleInput.setCurrentIndex(1)

            self.ui.mainTable.setRowCount(len(l))
            self.ui.mainTable.setColumnCount(5)

            self.ui.mainTable.setHorizontalHeaderLabels(
                ["Kullanıcı Adı", "E-Posta", "Doğum Tarihi", "Cinsiyet", "Rol"]
            )

            for i, row in enumerate(l):
                self.ui.mainTable.setItem(i, 0, QTableWidgetItem(row[1]))
                self.ui.mainTable.setItem(i, 1, QTableWidgetItem(row[3]))
                self.ui.mainTable.setItem(i, 2, QTableWidgetItem(row[4]))
                self.ui.mainTable.setItem(i, 3, QTableWidgetItem(row[6]))
                self.ui.mainTable.setItem(i, 4, QTableWidgetItem(row[8]))

        except Exception as e:
            raise e
        finally:
            con.close()

    def back(self):
        import view.homepagePanel as hp

        self.homepagePanel = hp.HomepagePanel(self.userData)
        self.homepagePanel.show()
        self.close()
