# -*- coding: utf-8 -*-

from tkinter import *

def b1_click():
    en3.delete(0, END)
    x = 0
    z = 0
    x = en1.get()
    y = 0
    y = en2.get()
    x = int(x)
    y = int(y)
    z = x + y
    en3.insert(0, z)
    
def b2_click():
    en3.delete(0, END)
    x = 0
    z = 0
    x = en1.get()
    y = 0
    y = en2.get()
    x = int(x)
    y = int(y)
    z = x - y
    en3.insert(0, z)    
    
def b3_click():
    en3.delete(0, END)
    x = 0
    z = 0
    x = en1.get()
    y = 0
    y = en2.get()
    x = int(x)
    y = int(y)
    z = x * y
    en3.insert(0, z)    
    
def b4_click():
    en3.delete(0, END)
    x = 0
    z = 0
    x = en1.get()
    y = 0
    y = en2.get()
    x = int(x)
    y = int(y)
    z = x / y
    en3.insert(0, z)    

def b5_click():
    en3.delete(0, END)
    
    

win = Tk()
win.geometry("750x400")
win.title("OLEH")
#win.resizable(width=False, height=False)

en1 = Entry(width = 50)
en2 = Entry(width = 50)
en3 = Entry(width = 72)
l1 = Label(text="Введите первое число",font=("Comic Sans MS", 12, "bold"))
l2 = Label(text="Введите второе число",font=("Comic Sans MS", 12, "bold"))
l3 = Label(text="Ответ",font=("Comic Sans MS", 12, "bold"))
b1 = Button(text="+",  width=15, height=4, bg='grey', font=("Comic Sans MS", 8, "bold"), command = b1_click)
b2 = Button(text="-",  width=15, height=4, bg='grey', font=("Comic Sans MS", 8, "bold"), command = b2_click)
b3 = Button(text="*",  width=15, height=4, bg='grey', font=("Comic Sans MS", 8, "bold"), command = b3_click)
b4 = Button(text="/",  width=15, height=4, bg='grey', font=("Comic Sans MS", 8, "bold"), command = b4_click)
b5 = Button(text="CE",  width=15, height=4, bg='grey', font=("Comic Sans MS", 8, "bold"), command = b5_click)
t1 = Text(width = 150, height = 150)

en1.place(x = 215, y = 15)
en2.place(x = 215, y = 45)
en3.place(x = 83, y = 205)
b1.place(x = 20, y = 100)
b2.place(x = 200, y = 100)
b3.place(x = 400, y = 100)
b4.place(x = 600, y = 100)
b5.place(x = 300, y = 250)
l1.place(x = 20, y = 10)
l2.place(x = 20, y = 40)
l3.place(x = 20, y = 200)
t1.place(x = 50, y = 150)


    
    
#x = en1
#y = en2
#b1 = x+y
#b2 = x-y
#b3 = x*y
#b4 = x/y
#en3 = b1




win.mainloop()
























#def bar():
    #if l1['bg'] == "#000000":
        #l1['bg'] = "#ffffff"
    #else:
        #l1['bg'] = "#000000"

#win = Tk()
#win.geometry("600x600")
#win.resizable(width=False, height=False)
#win.title("serafim")

#b1 = Button(text="Изменить",  width=28, height=4, bg='#ffaaaa', font=("Comic Sans MS", 8, "bold"), command=bar)

#en1  = Entry(width=50)

#b2 = Button(text="dfhsjhfk",  width=28, height=4, bg='#ffaaaa', font=("Comic Sans MS", 8, "bold"))
#l1 = Label(text="Text",font=("Comic Sans MS", 12, "bold"))

#b1.grid(row=0, column=0, pady=10, padx=10)
#en1.grid(row=0, column=2)
#b2.grid(row=1, column=1)
#l1.grid(row=0, column=1)





























 
 
#win = Tk()
#win.geometry("400x400");
#win.title('serafim');

#b1 = Button(text="Изменить",  width=28, height=4, bg='#ffaaaa', font=("Comic Sans MS", 8, "bold"))

##b1.grid(row=1, column=0)

#win.mainloop()