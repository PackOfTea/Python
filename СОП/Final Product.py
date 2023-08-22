# -*- coding: utf-8 -*-
from tkinter import *

win = Tk()
win.title("Title")

def login():
    if en1.get() != "" and en2.get() != "":
        import sqlite3
        con = sqlite3.connect("base.db")
        obj = con.cursor()
        obj.execute("SELECT user FROM users WHERE user='{}'".format(en1.get()))
        login = obj.fetchall()
        print(login)
        obj.execute("SELECT pass FROM users WHERE pass='{}'".format(en2.get()))
        passw = obj.fetchall()
        con.close()
        
        if en1.get() == login and en2.get() == passw:
            print("условие выплнено")
            a = Toplevel()
            a.geometry("300x300")
            l_1 = Label(text=res, font = ("Times New Roman", 12))
            l_1.pack()        
    else:
        from tkinter import messagebox
        messagebox.showinfo(title="Ошибка", message="Заполнены не все поля ввода")
    

en1 = Entry(width=30)
en2 = Entry(width=30)

b1 = Button(text="Вход", font=("Times New Roman", 12), command=login)
b2 = Button(text="Регистрация", font=("Times New Roman", 12))

l1 = Label(text="Логин", font=("Times New Roman", 12))
l2 = Label(text="Пароль", font=("Times New Roman", 12))

l1.pack()
en1.pack()
l2.pack()
en2.pack()
b1.pack()
b2.pack()

win.mainloop()