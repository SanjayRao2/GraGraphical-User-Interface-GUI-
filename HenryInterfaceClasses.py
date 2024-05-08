
class Author:
    def __init__(self, AUTHOR_NUM, AUTHOR_FIRST, AUTHOR_LAST):
        self.AUTHOR_NUM = AUTHOR_NUM
        self.AUTHOR_FIRST = AUTHOR_FIRST
        self.AUTHOR_LAST = AUTHOR_LAST

    def getAuthorNumber(self):
        return self.AUTHOR_NUM

    def __str__(self):
        return (f"{self.AUTHOR_FIRST} {self.AUTHOR_LAST}")

class Book:
    def __init__(self, BOOK_CODE = None, TITLE = None, PRICE = None):
        self.BOOK_CODE = BOOK_CODE
        self.TITLE = TITLE
        self.PRICE = PRICE

    def getBookCode(self):
        return self.BOOK_CODE

    def getPrice(self):
        return self.PRICE

    def __str__(self):
        return (f"{self.TITLE}")

class Branch:
    def __init__(self, BRANCH_NAME = None, ON_HAND = None):
        self.BRANCH_NAME = BRANCH_NAME
        self.ON_HAND = ON_HAND
        
    def get_branch_name(self):
        return self.BRANCH_NAME

    def get_on_hand(self):
        return self.ON_HAND

    def __str__(self):
        return (f"{self.BRANCH_NAME}")

class Price:
    def __init__(self, PRICE = None):
        self.PRICE = PRICE
 
    def get_price(self):
        return self.PRICE

    def __str__(self):
        return (f"{self.PRICE}")

class Category:
    def __init__(self, TYPE = None):
        self.TYPE = TYPE
        
    def getCategorytype(self):
        return self.TYPE

    def __str__(self):
        return (f"{self.TYPE}")

class Cat_Book:
    def __init__(self, TITLE = None, BOOK_CODE = None, PRICE = None):
        self.TITLE = TITLE
        self.BOOK_CODE = BOOK_CODE
        self.PRICE = PRICE

    def cat_getTitle(self):
        return self.TITLE

    def cat_getBookCode(self):
        return self.BOOK_CODE

    def cat_getPrice(self):
        return self.PRICE

    def __str__(self):
        return (f"{self.TITLE}")

class Cat_Price:
    def __init__(self, PRICE = None):
        self.PRICE = PRICE
 
    def cat_price(self):
        return self.PRICE

    def __str__(self):
        return (f"{self.PRICE}")

class Publisher:
    def __init__(self, PUBLISHER_NAME = None, PUBLISHER_CODE = None):
        self.PUBLISHER_NAME = PUBLISHER_NAME
        self.PUBLISHER_CODE = PUBLISHER_CODE
        
    def getPublisherName(self):
        return self.PUBLISHER_NAME

    def getPublisherCode(self):
        return self.PUBLISHER_CODE

    def __str__(self):
        return (f"{self.PUBLISHER_NAME}")

class Pub_Book:
    def __init__(self, TITLE = None, BOOK_CODE = None, PRICE = None):
        self.TITLE = TITLE
        self.BOOK_CODE = BOOK_CODE
        self.PRICE = PRICE

    def pub_getTitle(self):
        return self.TITLE
        
    def pub_getBookCode(self):
        return self.BOOK_CODE

    def pub_getPrice(self):
        return self.PRICE
    
    def __str__(self):
        return (f"{self.TITLE}")

class Pub_Price:
    def __init__(self, PRICE = None):
        self.PRICE = PRICE
 
    def get_price(self):
        return self.PRICE

    def __str__(self):
        return (f"{self.PRICE}")