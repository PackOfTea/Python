def akkerman(m,n):
    if m == 0:
        print (m,n)
        n+=1
        return n
    elif m>0 and n==0:
        print(m,n)
        return akkerman(m-1,1)
    elif m>0 and n>0:
        print(m,n)
        return akkerman(m-1,akkerman(m,n-1))
    
print(akkerman(2,0))