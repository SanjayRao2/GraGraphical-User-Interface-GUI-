import mysql.connector
from henryInterfaceClasses import Author, Book, Branch, Price, Category, Cat_Book, Cat_Price, Publisher, Pub_Book, Pub_Price

class HenryDAO():
    def __init__(self):
        self.mydb = mysql.connector.connect(
            user='root',
            passwd='root',
            database='comp3421',
            host='127.0.0.1')

        self.mycur = self.mydb.cursor()

    def getAuthorData(self):
        sql = "SELECT distinct(A.author_num), author_first, author_last FROM henry_author A LEFT JOIN henry_wrote W ON A.AUTHOR_NUM = W.AUTHOR_NUM WHERE W.AUTHOR_NUM IS NOT NULL ORDER BY w.author_num"
        self.mycur.execute(sql)

        data = []
        for row in self.mycur:
            data.append(Author(row[0], row[1], row[2]))
        return data

    def getBookData(self, auth_number):
        sql = f"SELECT b.book_code, title, price FROM HENRY_BOOK b JOIN HENRY_WROTE w ON b.book_code = w.book_code JOIN HENRY_AUTHOR a ON w.AUTHOR_NUM = a.AUTHOR_NUM WHERE (w.BOOK_CODE = b.BOOK_CODE) AND (w.AUTHOR_NUM like '{auth_number}')"
        self.mycur.execute(sql)

        data = []
        for row in self.mycur:
            data.append(Book(row[0], row[1], row[2]))
        return data

    def getBranchData(self, book_code):
        sql = f"select B.branch_name, I.on_hand from HENRY_BRANCH B JOIN HENRY_INVENTORY I ON B.BRANCH_NUM = I.BRANCH_NUM where B.BRANCH_NUM=I.BRANCH_NUM and I.BOOK_CODE='{book_code}'"
        self.mycur.execute(sql)

        data = []
        for row in self.mycur:
            data.append(Branch(row[0], row[1]))
        return data

    def getPriceData(self, BOOK_CODE, AUTHOR_NUM):
        sql = f"SELECT price from HENRY_BOOK B JOIN HENRY_WROTE W ON W.BOOK_CODE = B.BOOK_CODE WHERE (W.BOOK_CODE = '{BOOK_CODE}') AND (W.AUTHOR_NUM = '{AUTHOR_NUM}')"
        self.mycur.execute(sql)

        data = []
        for row in self.mycur:
            data.append(Price(row[0]))
        return data

    def getCategory(self):
        sql = "SELECT DISTINCT(type) From HENRY_BOOK"
        self.mycur.execute(sql)

        data = []
        for row in self.mycur:
            data.append(Category(row[0]))
        return data

    def getCategory_Book(self, TYPE):
        sql = f"SELECT title, book_code, price FROM HENRY_BOOK WHERE (type = '{TYPE}')"
        self.mycur.execute(sql)

        data = []
        for row in self.mycur:
            data.append(Cat_Book(row[0], row[1], row[2]))
        return data

    def cat_getPriceData(self, BOOK_CODE):
        sql = f"SELECT price from HENRY_BOOK WHERE BOOK_CODE = '{BOOK_CODE}'"
        self.mycur.execute(sql)

        data = []
        for row in self.mycur:
            data.append(Cat_Price(row[0]))
        return data

    def getPublisher(self):
        sql = "SELECT P.PUBLISHER_NAME, P.PUBLISHER_CODE FROM HENRY_publisher P LEFT OUTER JOIN henry_book B ON P.publisher_code = B.publisher_code GROUP BY B.PUBLISHER_CODE HAVING B.publisher_code is not null"
        self.mycur.execute(sql)

        data = []
        for row in self.mycur:
            data.append(Publisher(row[0], row[1]))
        return data

    def getPublisher_Book(self, PUBLISHER_CODE):
        sql = f"SELECT title, book_code, price FROM HENRY_BOOK WHERE (PUBLISHER_CODE = '{PUBLISHER_CODE}')"
        self.mycur.execute(sql)

        data = []
        for row in self.mycur:
            data.append(Pub_Book(row[0], row[1], row[2]))
        return data

    def pub_getPriceData(self, BOOK_CODE, PUBLISHER_CODE):
        sql = f"SELECT price from HENRY_BOOK WHERE (BOOK_CODE = '{BOOK_CODE}') AND (PUBLISHER_CODE = '{PUBLISHER_CODE}')"
        self.mycur.execute(sql)

        data = []
        for row in self.mycur:
            data.append(Pub_Price(row[0]))
        return data

    def close(self):
        self.mydb.commit()
        self.mydb.close()
obj = HenryDAO()