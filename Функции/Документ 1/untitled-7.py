# -*- coding: utf-8 -*-

x = int(input("аргумент"))

import math

def area(dl):
    if x>0:
        print("аргумент положительный")
    else:
        print("аргумент отрицательный")
    
    return math.factorial(x)


f = area(x)
print(f)