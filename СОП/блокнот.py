# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import messagebox

def read():
    f = open((en1.get() + ".txt"), "r")
    i = f.readlines()
    i = "".join(i)
    f.close()
    text.insert(1.0, i)

def update():
    f = open((en1.get() + ".txt"), "w")
    f.write(text.get(1.0, END))
    f.close()
    messagebox.showinfo(title="Результат", message="Готово")

def clear():
    text.delete(1.0, END)
    
win = Tk()
win.geometry("800x600")
win.title("Notepad")

en1 = Entry(width = 50)
text = Text(width = 50, height = 25)
l1 = Label(text="Имя файла", font=("Comic Sans MS", 10, "bold"))
l2 = Label(text="Информация", font=("Comic Sans MS", 10, "bold"))
b1 = Button(text="open", width = 5, height = 2, font=("Comic Sans MS", 8, "bold"), command = read)
b2 = Button(text="update", width = 5, height = 2, font=("Comic Sans MS", 8, "bold"), command = update)
b3 = Button(text="clear", width = 5, height = 2, font=("Comic Sans MS", 8, "bold"), command = clear)


en1.place(x = 250, y = 50)
text.place(x = 200, y = 70)
l1.place(x = 100, y = 45)
l2.place(x = 100, y = 65)
b1.place(x = 330, y = 480)
b2.place(x = 380, y = 480)
b3.place(x = 430, y = 480)


win.mainloop()