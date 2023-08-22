# -*- coding: utf-8 -*-

from debees import *

db1 = FileDB("file1.txt")




#print(db1.read())


#db1.adder("qwerty")

#print(db1.read())
#print("***")

#db1.clear()

#print("***")
#print(db1.read())
#print("***")

print(db1.fName)

com= ""
while com != "exit":
    com = str(input("какую команду выполнить? "))
    if com == "read":
        print(db1.read())
    elif com == "add":
        text = str(input("какие данные добавить? "))
        db1.adder(text)
    elif com == "clear":
        db1.clear()
    elif com == "exit":
        print("вы вышли из программы")
    else:
        print("введите одну из данных команд - \"read\", \"add\", \"clear\", \"exit\"")