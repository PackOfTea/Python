a=10
b=1

def f(n1, n2):
        if n1 <= n2:
            print(n1)
            f(n1 + 1, n2)
        
        if n1 >= n2:
            
            f(n2 + 1, n1)
            print(n2)
            
print (f(a,b))