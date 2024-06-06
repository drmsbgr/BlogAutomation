import sqlite3
from data.account import *
from data.comment import *

DBNAME = "blog.db"


def connectDB():
    return sqlite3.connect(DBNAME)


def initializeDB():
    con = connectDB()
    cur = con.cursor()

    try:
        cur.execute(
            """CREATE TABLE IF NOT EXISTS roles (
                role_ID INTEGER NOT NULL UNIQUE,
                role_NAME TEXT NOT NULL,
                PRIMARY KEY("role_ID" AUTOINCREMENT)
                )""",
            (),
        )

        cur.execute(
            """CREATE TABLE IF NOT EXISTS genders (
                gender_ID INTEGER NOT NULL UNIQUE,
                gender_NAME TEXT NOT NULL,
                PRIMARY KEY("gender_ID" AUTOINCREMENT)
                )""",
            (),
        )

        if (
            cur.execute("SELECT gender_ID FROM genders WHERE gender_ID = 1").fetchone()
            == None
        ):
            cur.execute("""INSERT INTO genders VALUES (1,?)""", ("Erkek",))

        if (
            cur.execute("SELECT gender_ID FROM genders WHERE gender_ID = 2").fetchone()
            == None
        ):
            cur.execute("""INSERT INTO genders VALUES (2,?)""", ("Kadın",))

        if (
            cur.execute("SELECT gender_ID FROM genders WHERE gender_ID = 3").fetchone()
            == None
        ):
            cur.execute(
                """INSERT INTO genders VALUES (3,?)""", ("Belirtmek İstemiyorum",)
            )

        cur.execute(
            """CREATE TABLE IF NOT EXISTS accounts (
                account_ID INTEGER NOT NULL UNIQUE,
                account_USERNAME TEXT NOT NULL UNIQUE,
                account_PASSWORD TEXT NOT NULL,
                account_MAIL TEXT NOT NULL,
                account_GENDER_ID INTEGER NOT NULL,
                account_BIRTHDATE TEXT NOT NULL,
                account_ROLE_ID INTEGER NOT NULL,
                PRIMARY KEY("account_ID" AUTOINCREMENT)
                FOREIGN KEY("account_ROLE_ID") REFERENCES "roles"("role_ID"),
                FOREIGN KEY("account_GENDER_ID") REFERENCES "genders"("gender_ID")
                )""",
            (),
        )

        if (
            cur.execute("SELECT role_ID FROM roles WHERE role_ID = 1").fetchone()
            == None
        ):
            cur.execute("""INSERT INTO roles VALUES (1,?)""", ("YÖNETİCİ",))

        if (
            cur.execute("SELECT role_ID FROM roles WHERE role_ID = 2").fetchone()
            == None
        ):
            cur.execute("""INSERT INTO roles VALUES (2,?)""", ("ÜYE",))

        if (
            cur.execute(
                "SELECT account_ID FROM accounts WHERE account_ID = 1"
            ).fetchone()
            == None
        ):
            cur.execute(
                """INSERT INTO accounts VALUES (1,?,?,?,?,?,?)""",
                ("admin", "123", "drmsbgr@gmail.com", 1, "18.04.2005", 1),
            )

        cur.execute(
            """CREATE TABLE IF NOT EXISTS posts (
                post_ID INTEGER NOT NULL UNIQUE,
                post_HEADER TEXT NOT NULL,
                post_CONTENT TEXT NOT NULL,
                post_DATE TEXT NOT NULL,
                post_OWNER_ID INTEGER NOT NULL,
                PRIMARY KEY("post_ID" AUTOINCREMENT),
                FOREIGN KEY("post_OWNER_ID") REFERENCES "accounts"("account_ID")
                )""",
            (),
        )

        cur.execute(
            """CREATE TABLE IF NOT EXISTS categories (
                category_ID INTEGER NOT NULL UNIQUE,
                category_NAME TEXT NOT NULL,
                PRIMARY KEY("category_ID" AUTOINCREMENT)
                )""",
            (),
        )

        cur.execute(
            """CREATE TABLE IF NOT EXISTS postCategories (
                postCategory_ID INTEGER NOT NULL UNIQUE,
                post_ID INTEGER NOT NULL,
                category_ID INTEGER NOT NULL,
                PRIMARY KEY("postCategory_ID" AUTOINCREMENT),
                FOREIGN KEY("post_ID") REFERENCES "posts"("post_ID"),
                FOREIGN KEY("category_ID") REFERENCES "categories"("category_ID")
                )""",
            (),
        )

        cur.execute(
            """CREATE TABLE IF NOT EXISTS comments (
                comment_ID INTEGER NOT NULL UNIQUE,
                comment_OWNER_ID INTEGER NOT NULL,
                comment_POST_ID INTEGER NOT NULL,
                comment_CONTENT TEXT NOT NULL,
                comment_DATE TEXT NOT NULL,
                PRIMARY KEY("comment_ID" AUTOINCREMENT),
                FOREIGN KEY("comment_OWNER_ID") REFERENCES "accounts"("account_ID"),
                FOREIGN KEY("comment_POST_ID") REFERENCES "posts"("post_ID")
                )""",
            (),
        )

        con.commit()
        con.close()

    except Exception as e:
        raise e
    finally:
        con.close()


def getAccountById(id) -> Account:
    try:
        con = connectDB()
        cur = con.cursor()
        sql = """SELECT * FROM accounts WHERE account_ID=?"""
        row = cur.execute(sql, (id,)).fetchone()
        return Account(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
    except Exception as e:
        raise e
    finally:
        con.close()


def getCommentsByPostId(id):
    try:
        con = connectDB()
        cur = con.cursor()
        sql = """SELECT * FROM comments 
        WHERE comment_POST_ID=?
        ORDER BY comment_ID DESC"""

        l = cur.execute(sql, (id,)).fetchall()

        return [Comment(row[0], row[1], row[2], row[3], row[4]) for row in l]

    except Exception as e:
        raise e
    finally:
        con.close()


def getCategoriesByPostId(id):
    try:
        con = connectDB()
        cur = con.cursor()
        sql = """SELECT postCategory_ID,categories.category_ID,category_NAME FROM postCategories 
        INNER JOIN categories 
        ON postCategories.category_ID=categories.category_ID
        WHERE post_ID=?"""

        l = cur.execute(sql, (id,)).fetchall()

        return [row[2] for row in l]

    except Exception as e:
        raise e
    finally:
        con.close()
