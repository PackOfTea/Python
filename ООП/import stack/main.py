# -*- coding: utf-8 -*-

from classes import *

x = input("Выберите метод чтения стека (filo или fifo): ")
i = 0

if x == "filo":
    s = Filo(5)
elif x== "fifo":
    s = Fifo(5)
else:
    print("НЕТ ТАКОЙ КОМАНДЫ!!!")

while i != s.mx:
    s.push(input("Введите данные: "))
    i += 1


print(s.front())
print(s.back())
print(s.size())


#s.push(5)
#s.push(9)
#s.push(3)
#s.push(1)
#s.push(5)
#s.push(9)
#s.push(3)
#s.push(1)
#s.push(5)
#s.push(9)

print(s.show())

print(s.pop())
print(s.pop())
print(s.pop())
s.clear()
print(s.pop())
print(s.pop())


print(s.show())