# -*- coding: utf-8 -*-
def function(num):
    arr=["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    if num>=1 and num<=7:
        return arr[num-1]
    else:
        return "вы ввели неверное число"
    print(function(int(input("Введите число"))))
