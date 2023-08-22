# -*- coding: utf-8 -*-

d = int(input("Длина "))
s = int(input("Ширина "))

def area(dl,shr):
    if dl==shr:
        print("Ошибка! Это квадрат!")
    else:
        return dl*shr

f = area(d,s)
print(f)