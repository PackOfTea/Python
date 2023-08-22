def get_users():
    file = open("userss/users.txt", "r")
    data = file.read()
    file.close()
    arr = data.split('\n')
    print(arr)
    arr_users = []
    for i in range (0,len(arr),1):
        b = arr[i]
        c = [b.split(' ')]
        print(c)
        arr_users = arr_users + c
    return arr_users
        
    
main_arr = get_users()

print(main_arr)

def check_login(log, arr_users):
    flag = False
    for i in range (0,len(arr_users),1):
        if log == arr_users[i][0]:
            print (arr_users[i][0])
            flag = True
        
    return flag
    
print(check_login("alsssslo", main_arr))