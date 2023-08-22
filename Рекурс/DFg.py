a=10
b=1

def f(n1, n2):
        if n1 >= n2:
            print(n1)
            f(n1 - 1, n2)
            
print (f(a,b))