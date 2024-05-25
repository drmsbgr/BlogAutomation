import sqlite3

DBNAME = "blog.db"


def connectDB():
    return sqlite3.connect(DBNAME)


def initializeDB():
    con = connectDB()
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS accounts (
        account_ID INTEGER NOT NULL UNIQUE,
        account_USERNAME TEXT NOT NULL UNIQUE,
        account_PASSWORD TEXT NOT NULL,
        account_GENDER INTEGER NOT NULL,
        account_BIRTHDATE TEXT NOT NULL,
        PRIMARY KEY("account_ID" AUTOINCREMENT)
        )""", ())
