def rec(n):
    if n == 1:
        print (n)
    else:
        rec(n-1)
        print(n)

rec(10)