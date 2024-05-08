import tkinter as tk
from tkinter import *
from tkinter.ttk import Combobox, Notebook, Treeview
from henryDAO import HenryDAO

class HenrySBA(Frame):
    dao = HenryDAO()
    auth_data = []
    books_data = []
    price = 0
    auth_number = 0
    book_number = 0

    def __init__(self,name,*args,**kwargs):
        global price, auth_number, book_number
        price = StringVar()
        Frame.__init__(self,*args,**kwargs)

        self.label = Label(self, text="Author Selection")
        self.label.grid(row=15,column=1)
        auth_comb = Combobox(self, width = 20, state="readonly")
        auth_comb.grid(column=1, row=16)
        self.auth_data = self.dao.getAuthorData()
        if(len(self.auth_data)>0):
            auth_number=(self.auth_data[0]).getAuthorNumber()
        auth_comb['values'] = self.auth_data
        auth_comb.current(0)
        auth_comb.bind("<<ComboboxSelected>>", self.auth_comb_callback)

        self.label = Label(self, text="Book Selection")
        self.label.grid(row=15,column=5)
        self.book_comb = Combobox(self, width = 20, state="readonly")
        self.book_comb.grid(column=5, row=16)
        self.books_data = self.dao.getBookData(auth_number)
        if(len(self.books_data)>0):
            book_number=(self.books_data[0]).getBookCode()
            price.set((self.books_data[0]).getPrice())
        self.book_comb['values'] = self.books_data
        self.book_comb.current(0)
        self.book_comb.bind("<<ComboboxSelected>>", self.book_comb_callback)

        self.tree1 = Treeview(self, columns=('Branch Name', 'Copies Available'), show='headings')
        self.tree1.heading('Branch Name', text='Branch Name')
        self.tree1.heading('Copies Available', text='Copies Available')
        self.tree1.grid(column=1, row=1)

        for i in self.tree1.get_children():
            self.tree1.delete(i)

        self.branch_data = self.dao.getBranchData(book_number)
        for row in self.branch_data:
            self.tree1.insert("", "end", values=[row.get_branch_name(), row.get_on_hand()])

        self.label = Label(self, text="Price: ")
        self.label.grid(row=1,column=6)
        self.label = Label(self, textvariable=price)
        self.label.grid(row=1,column=9)

    def auth_comb_callback(self, event):
        global price,auth_number, book_number
        selIndex = event.widget.current()
        auth_number = self.auth_data[selIndex].getAuthorNumber()
        self.books_data = self.dao.getBookData(auth_number)
        self.book_comb['values'] = self.books_data
        self.book_comb.current(0)
        book_number = self.books_data[0].getBookCode()
        price.set(self.dao.getPriceData(book_number, auth_number))

        for i in self.tree1.get_children():
            self.tree1.delete(i)

        self.branch_data = self.dao.getBranchData(book_number)
        for row in self.branch_data:
            self.tree1.insert("", "end", values=[row.get_branch_name(), row.get_on_hand()])
        print(f" Index selected is: {str(selIndex)} And Author Num is: {str(self.auth_data[selIndex].getAuthorNumber())}")

    def book_comb_callback(self, event):
        global price, auth_number
        selIndex = event.widget.current()
        print(f" Index selected is: {str(selIndex)} And Book Code is: {str(self.books_data[selIndex].getBookCode())}")

        for i in self.tree1.get_children():
            self.tree1.delete(i)

        self.branch_data = self.dao.getBranchData(self.books_data[selIndex].getBookCode())
        for row in self.branch_data:
            self.tree1.insert("", "end", values=[row.get_branch_name(), row.get_on_hand()])

        price.set(self.dao.getPriceData(self.books_data[selIndex].getBookCode(),auth_number))

class HenrySBC(Frame):
    dao = HenryDAO()
    cat_data = []
    cat_book_data = []
    cat_price = 0
    cat_number = 0
    cat_book_number = 0

    def __init__(self,name,*args,**kwargs):
        global cat_price, cat_number, cat_book_number
        cat_price = StringVar()
        Frame.__init__(self,*args,**kwargs)

        self.label = Label(self, text="Book Category")
        self.label.grid(row=15,column=1)
        cat_comb = Combobox(self, width = 20, state="readonly")
        cat_comb.grid(column=1, row=16)
        self.cat_data = self.dao.getCategory()
        if(len(self.cat_data)>0):
            cat_number=(self.cat_data[0]).getCategorytype()
        cat_comb['values'] = self.cat_data
        cat_comb.current(0)
        cat_comb.bind("<<ComboboxSelected>>", self.cat_comb_callback)

        self.label = Label(self, text="Book Selection")
        self.label.grid(row=15,column=5)
        self.cat_book_comb = Combobox(self, width = 20, state="readonly")
        self.cat_book_comb.grid(column=5, row=16)
        self.cat_book_data = self.dao.getCategory_Book(cat_number)
        if(len(self.cat_book_data)>0):
            cat_book_number=(self.cat_book_data[0]).cat_getBookCode()
            cat_price.set((self.cat_book_data[0]).cat_getPrice())
        self.cat_book_comb['values'] = self.cat_book_data
        self.cat_book_comb.current(0)
        self.cat_book_comb.bind("<<ComboboxSelected>>", self.cat_book_comb_callback)

        Treeview
        self.tree1 = Treeview(self, columns=('Branch Name', 'Copies Available'), show='headings')
        self.tree1.heading('Branch Name', text='Branch Name')
        self.tree1.heading('Copies Available', text='Copies Available')
        self.tree1.grid(column=1, row=1)

        for i in self.tree1.get_children():
            self.tree1.delete(i)

        self.branch_data = self.dao.getBranchData(cat_book_number)
        for row in self.branch_data:
            self.tree1.insert("", "end", values=[row.get_branch_name(), row.get_on_hand()])

        self.label = Label(self, text="Price: ")
        self.label.grid(row=1,column=6)
        self.label = Label(self, textvariable=cat_price)
        self.label.grid(row=1,column=9)

    def cat_comb_callback(self, event):
        global cat_price, cat_number, cat_book_number
        selIndex = event.widget.current()
        cat_number = self.cat_data[selIndex].getCategorytype()
        self.cat_book_data = self.dao.getCategory_Book(cat_number)
        self.cat_book_comb['values'] = self.cat_book_data
        self.cat_book_comb.current(0)
        cat_book_number = self.cat_book_data[0].cat_getBookCode()
        cat_price.set(self.dao.cat_getPriceData(cat_book_number))
                
        for i in self.tree1.get_children():
            self.tree1.delete(i)

        self.branch_data = self.dao.getBranchData(cat_book_number)
        
        for row in self.branch_data:
            self.tree1.insert("", "end", values=[row.get_branch_name(), row.get_on_hand()])
        print(f" Index selected is: {str(selIndex)} And Category type is: {cat_number}")

    def cat_book_comb_callback(self, event):
        global cat_price, cat_number, cat_book_number
        selIndex = event.widget.current()
        print(f" Index selected is: {str(selIndex)} And Book Code is: {str(self.cat_book_data[selIndex].cat_getBookCode())}")

        for i in self.tree1.get_children():
            self.tree1.delete(i)

        self.branch_data = self.dao.getBranchData(self.cat_book_data[selIndex].cat_getBookCode())
        for row in self.branch_data:
            self.tree1.insert("", "end", values=[row.get_branch_name(), row.get_on_hand()])
        
        cat_price.set(self.dao.cat_getPriceData(self.cat_book_data[selIndex].cat_getBookCode()))
                
class HenrySBP(Frame):
    dao = HenryDAO()
    pub_data = []
    pub_book_data = []
    pub_price = 0
    pub_number = 0
    pub_book_number = 0

    def __init__(self,name,*args,**kwargs):
        global pub_price, pub_book_number, pub_number
        pub_price = StringVar()
        Frame.__init__(self,*args,**kwargs)

        # Search by Publisher
        self.label = Label(self, text="Publisher")
        self.label.grid(row=15,column=1)
        pub_comb = Combobox(self, width = 20, state="readonly")
        pub_comb.grid(column=1, row=16)
        self.pub_data = self.dao.getPublisher()
        if(len(self.pub_data)>0):
            pub_number=(self.pub_data[0]).getPublisherCode()
        pub_comb['values'] = self.pub_data
        pub_comb.current(0)
        pub_comb.bind("<<ComboboxSelected>>", self.pub_comb_callback)

        self.label = Label(self, text="Book Selection")
        self.label.grid(row=15,column=5)
        self.pub_book_comb = Combobox(self, width = 20, state="readonly")
        self.pub_book_comb.grid(column=5, row=16)
        self.pub_book_data = self.dao.getPublisher_Book(pub_number)
        if(len(self.pub_book_data)>0):
            pub_book_number = (self.pub_book_data[0]).pub_getBookCode()
            pub_price.set((self.pub_book_data[0]).pub_getPrice())
        self.pub_book_comb['values'] = self.pub_book_data
        self.pub_book_comb.current(0)
        self.pub_book_comb.bind("<<ComboboxSelected>>", self.pub_book_comb_callback)

        Treeview
        self.tree1 = Treeview(self, columns=('Branch Name', 'Copies Available'), show='headings')
        self.tree1.heading('Branch Name', text='Branch Name')
        self.tree1.heading('Copies Available', text='Copies Available')
        self.tree1.grid(column=1, row=1)

        for i in self.tree1.get_children():
            self.tree1.delete(i)

        self.branch_data = self.dao.getBranchData(pub_book_number)
        for row in self.branch_data:
            self.tree1.insert("", "end", values=[row.get_branch_name(), row.get_on_hand()])

        self.label = Label(self, text="Price: ")
        self.label.grid(row=1,column=6)
        self.label = Label(self, textvariable=pub_price)
        self.label.grid(row=1,column=9)

    def pub_comb_callback(self, event):
        global pub_price, pub_number, pub_book_number
        selIndex = event.widget.current()
        pub_number = self.pub_data[selIndex].getPublisherCode()
        self.pub_book_data = self.dao.getPublisher_Book(pub_number)
        self.pub_book_comb['values'] = self.pub_book_data
        self.pub_book_comb.current(0)
        pub_book_number = self.pub_book_data[0].pub_getBookCode()
        pub_price.set(self.dao.pub_getPriceData(pub_book_number, pub_number))
        
        for i in self.tree1.get_children():
            self.tree1.delete(i)

        self.branch_data = self.dao.getBranchData(pub_book_number)
        for row in self.branch_data:
            self.tree1.insert("", "end", values=[row.get_branch_name(), row.get_on_hand()])
        print(f" Index selected is: {str(selIndex)} And Publisher Name is: {pub_number}")

    def pub_book_comb_callback(self, event):
        global pub_price, pub_number, pub_book_number
        selIndex = event.widget.current()
        print(f" Index selected is: {str(selIndex)} And Book Code is: {str(self.pub_book_data[selIndex].pub_getBookCode())}")

        for i in self.tree1.get_children():
            self.tree1.delete(i)

        self.branch_data = self.dao.getBranchData(self.pub_book_data[selIndex].pub_getBookCode())
        
        for row in self.branch_data:
            self.tree1.insert("", "end", values=[row.get_branch_name(), row.get_on_hand()])

        pub_price.set(self.dao.pub_getPriceData(self.pub_book_data[selIndex].pub_getBookCode(), pub_number))

root = tk.Tk()
root.title("Henry Bookstore")
root.geometry('800x400')

tabControl = Notebook(root)
tab1 = HenrySBA(tabControl)
tab2 = HenrySBC(tabControl)
tab3 = HenrySBP(tabControl)
tabControl.add(tab1, text ='Search by Author')
tabControl.add(tab2, text ='Search by Category')
tabControl.add(tab3, text ='Search by Publisher')
tabControl.pack(expand = 1, fill ="both")

root.mainloop()