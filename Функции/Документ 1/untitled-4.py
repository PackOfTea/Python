# -*- coding: utf-8 -*-

func = 0
x = float(input("число "))

def area(peremennaya1):
    if x <= 1:
        return 1
    elif x > 1 and x <= 2:
        return 0
    elif x > 2 and x <= 10:
        return 2*x
    elif x > 10:
        return x*x

func = area(x)
print(func)