def gen_array(a1,a2,a3):
    arr = []
    for i in range (a1,a2,a3):
        arr[i]=i
    return arr


print (gen_array(5,11,1))