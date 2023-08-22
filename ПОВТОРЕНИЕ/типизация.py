# -*- coding: utf-8 -*-
def func1(a: int) -> bool:
    return (a % 2) == 1

def func2(a: list) -> int:
    summ = 0
    for i in range (0, len(a), 1):
        summ = summ + a[i]
    return summ

def func3(a: int) -> int:
    fact = 1
    for i in range (1, a + 1, 1):
        fact = fact * i 
    return fact

def func4(a: int) -> list:
    """  """
    summ3 = 0
    summ2 = 1
    summ1 = 0
    i = 0
    arr = []
    while i != a:
        summ1 = summ2 + summ3
        summ3 = summ2
        summ2 = summ1
        arr.append(summ1)
        i += 1
    return arr


def sumArray(arr1: list, arr2: list) -> list:
    arr3 = []
    
    
    
    #for i in range (0, len(arr1)):
    
    
    #r = 0
    
    #if len(arr1) < len(arr2):
        #for i in range (0, len(arr2), 1):
            #if arr1[i] != ['']:
                #arr3.append(arr1[i] + arr2[i])
                #print("AZAZAZAZAZAZA")            
                #r += 1
            #arr3.append(arr1[0:len(arr1) - r:1])
    #else:
        #for i in range (0, len(arr1), 1):
            #arr3.append(arr1[i] + arr2[i])
            #arr3.append(arr2[i])
        
    #return arr3
        
def gen_array(nach: int, kon: int, shag: int) -> list:
    arr = []
    for i in range (nach, kon + 1, shag):
        arr.append(i)
        
    return arr


def inArray(zn: int, arr: list) -> bool:
    for i in range (0, len(arr), 1):
        if zn == arr[i]:
            return True
        
print(func1(23))
print(func2([2, 9, 884, 8, 84, 8, 8946, 4, 846, 68, 46, 155, 4]))
print(func3(5))
print(func4(8))
#print(sumArray([45, 45, 45, 2554, 4, 5, 45454, 848], [545, 4154, 54, 545, 484, 5138, 535, 34120, 213, 852, 8]))
print(gen_array(0, 2000, 50))
print(inArray(8, [1, 2, 3, 4, 5, 6, 7, 8, 9, 5, 5, 15, 11, 251322, 313, 12]))