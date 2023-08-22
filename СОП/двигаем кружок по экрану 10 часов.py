from tkinter import *

def movU(e):
    coord = c.coords(ball)
    if coord[1] >= 10.0 and coord[3] >= 50.0:
        c.move(ball, 0, -5)
        print(c.coords(ball))

def movD(e):
    coord = c.coords(ball)
    if coord[1] <= 355.0 and coord[3] <= 395.0:
        c.move(ball, 0, 5)
        print(c.coords(ball))

def movL(e):
    coord = c.coords(ball)
    if coord[0] >= 10.0 and coord[2] >= 50.0:
        c.move(ball, -5, 0)
        print(c.coords(ball))

def movR(e):
    coord = c.coords(ball)
    if coord[0] <= 355.0 and coord[2] <= 395.0:
        c.move(ball, 5, 0)
        print(c.coords(ball))

root = Tk()
c = Canvas(width=400, height=400, bg="blue")
c1 = Canvas(width=400, height=200, bg="green")
c.focus_set()
c.pack()
c1.pack()

ball = c.create_oval(140, 140, 180, 180, fill="yellow")

c.bind("<Up>", movU)
c.bind("<Down>", movD)
c.bind("<Left>", movL)
c.bind("<Right>", movR)

root.mainloop()