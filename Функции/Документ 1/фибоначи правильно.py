# -*- coding: utf-8 -*-


def area():
    n = int(input("количество чисел Фибоначчи - "))
    i=0        
    summ3=0
    summ2=1
    summ1=0      
    while i!=n:
        summ1 = summ2 + summ3
        summ3=summ2
        summ2=summ1
        i+=1
    return summ1

print(area())
