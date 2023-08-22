# -*- coding: utf-8 -*-

class Item():
    def __init__(self, num, nm, nsh, prc):
        self.num = num
        self.nmItem = nm
        self.nmShop = nsh
        self.price = prc
        
class Warehouse():
    def __init__(self):
        self.database = []
               
    def addItem(self, item):
        self.database.append(item)
    def showItemInfo(self):
        for i in self.database:
            print(i.num, i.nmItem, i.nmShop, i.price)
            


w = Warehouse()
#item1 = Item(1, "playstation five", "DNS", 0)
#w.addItem(item1)
#item2 = Item((len(w.database) + 1), "xbox", "MVideo", 15)
#w.addItem(item2)
#item3 = Item((len(w.database) + 1), "iphone", "Sitilink", 9999999999999990)
#w.addItem(item3)
#w.showItemInfo()

import id_number

x = input("komanda ")
while x == "go":
    item = Item((len(w.database) + 1), input("tovar "), input("magasin "), int(input("tsena ")))
    w.addItem(item)
    print(id_number.number(len(w.database)))
    w.showItemInfo()
    
    x = input("komanda ")
    
#def adder():
    #neym = input("vvedite nazvanie tovara")
    #w.addItem(i.num, (len(i.num) + 1), neym)
    #print(i.num)    
        

        
#i = Item()
#w = Warehouse()
#print(w.database)
#w.addItem(i.num, (len(i.num) + 1))
#print(i.num)



#while True:
    #x = input("komanda")
    #if x == "add":
        #adder()