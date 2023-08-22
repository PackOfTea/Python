def SumRange(a: int, b: int) -> int:
    summ = 0
    if a < b:
        for i in range(a,b + 1,1):
            summ = summ + i
        return summ
    else:
        return 0
    
    
    
def Calc(a: int, b: int, op: int) -> int:
    if op == 0:
        return a+b
    if op == 1:
        return a-b
    if op == 2:
        return a*b
    if op == 3:
        return a/b
    
    
def Quarter(x: int, y: int) -> int:
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x > 0 and y < 0:
        return 4
    elif x < 0 and y < 0:
        return 3
    else:
        return 0
print(SumRange(1,3))
print(Calc(10,2,0))
print(Calc(10,2,1))
print(Calc(10,2,2))
print(Calc(10,2,3))
print(Quarter(1,3))