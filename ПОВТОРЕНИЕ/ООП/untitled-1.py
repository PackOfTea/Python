class User():
    def __init__(self, msg, friends):
        self.msg = msg
        self.fr = friends
    
    def MinusMsg(self):
        self.msg -= 1
    def PlusMsg(self):
        self.msg += 1
    
    def MinusFriend(self):
        self.fr -= 1
    def PlusFriend(self):
        self.fr += 1        
    
    
id1 = User(0, 0)
print(id1.msg, id1.fr)

com = True
while com == True:
    inp = input("введите команду")
    
    if inp == "- сообщение":
        id1.MinusMsg()
    elif inp == "+ сообщение":
        id1.PlusMsg()
    elif inp == "- друг":
        id1.MinusFriend()
    elif inp == "+ друг":
        id1.PlusFriend()
    else:
        com = False
    print(id1.msg, id1.fr)