# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import messagebox

def read():
    f = open((en1.get() + ".txt"), "r")
    i = f.readlines()
    i = "".join(i)
    f.close()
    en2.insert(0, i)

def update():
    f = open((en1.get() + ".txt"), "w")
    f.write(en2.get(0, END))
    f.close()
    messagebox.showinfo(title="Результат", message="Готово")

def clear():
    en2.delete(0, END)


def login():
    import sqlite3
    
    con = sqlite3.connect('base.db')
    obj = con.cursor()
    obj.execute("SELECT * FROM users WHERE user='{}' AND login='{}'".format(en1.get(), en2.get()))
    res = obj.fetchall()
    print(res)
    

        
    
def reg():
    import sqlite3
    
    win2 = Tk()
    win2.geometry("500x500")
    win2.title("Регистрация")
    
    def close():
        if en2_1.get() != "" and en2_2.get() != "" and en2_3.get() != "":
            if en2_2.get() == en2_3.get():
                con = sqlite3.connect('base.db')
                obj = con.cursor()
                obj.execute("INSERT INTO users VALUES ('" + en2_1.get() + "', '" + en2_2.get() + "')")
                con.commit()
                con.close()
                win2.destroy()
            else:
                messagebox.showinfo(title="ЕБАЛАЙ, ПОСМОТРИ И НАПИШИ ОДИНАКОВЫЕ ПАРОЛИ", message="ПАРОЛИ НЕ СОВПАДАЮТ")
        
        
        
        
    
    en2_1 = Entry(width = 40)
    en2_2 = Entry(width = 40)
    en2_3 = Entry(width = 40)
    l2_1 = Label(text = "Введите логин", font=("Comic Sans MS", 10, "bold"))
    l2_2 = Label(text = "Введите пароль", font=("Comic Sans MS", 10, "bold"))
    l2_3 = Label(text = "Введите пароль ещё раз", font=("Comic Sans MS", 10, "bold"))
    b2_1 = Button(text="Зарегистрировать", width=5, height=2, font=("Comic Sans MS", 8, "bold"), command=close)
    
    en2_1.place(x = 50, y = 50)
    en2_2.place(x = 50, y = 75)
    en2_3.place(x = 50, y = 100)
    l2_1.place(x = 150, y = 55) 
    l2_2.place(x = 150, y = 80)
    l2_3.place(x = 150, y = 105)
    b2_1.place(x = 200, y = 200)
    
    

    
win = Tk()
win.geometry("800x300")
win.title("ВКонтакте")

en1 = Entry(width = 50)
en2 = Entry(width = 50)
l1 = Label(text="Логин", font=("Comic Sans MS", 10, "bold"))
l2 = Label(text="Пароль", font=("Comic Sans MS", 10, "bold"))
b1 = Button(text="LOG IN", width = 5, height = 2, font=("Comic Sans MS", 8, "bold"), command = login)
b2 = Button(text="registration", width = 15, height = 2, font=("Comic Sans MS", 8, "bold"), command = reg)


en1.place(x = 250, y = 50)
en2.place(x = 200, y = 70)
l1.place(x = 100, y = 45)
l2.place(x = 100, y = 65)
b1.place(x = 330, y = 180)
b2.place(x = 380, y = 180)

win.mainloop()