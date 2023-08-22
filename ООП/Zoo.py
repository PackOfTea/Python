# -*- coding: utf-8 -*-

class Politpet():
    def hi(self):
        print("Салам, я " + self.breed + " " + self.nm)
    
    def hit_self(self):
        self.hp -= self.hit
    
    def hit_it(self, target):
        target.hp -= self.hit
        
    def othil (self):
        self.regen = 50
        if self.mana > 40:
            self.hp += self.regen
            self.mana -= 40         
        
class Putin(Politpet):
    def __init__(self, name):
        self.hp = 100
        self.hit = 1000
        self.mana = 100
        self.breed = "Владимир"
        self.nm = name
    def thief(self):
        print("Своровал твою жизнь")

class Peskov(Politpet):
    def __init__(self, name):
        self.hp = 100
        self.hit = 300
        self.mana = 200
        self.breed = "Димас"
        self.nm = name
    def lier(self):
        print ("Вешаю лапшу на уши 10 часов уже 15 лет")
        
        
        
class Medvedev(Politpet):
        def __init__(self, name):
            self.hp = 100
            self.hit = 300
            self.mana = 200
            self.breed = "Димон"
            self.nm = name
        def expremier(self):
            print ("Эппл напрягся, в общем")   
        
        
p1 = Putin("Путин")
p1.hi()
p1.thief()
p2 = Peskov("Песков")
p2.hi()
p2.lier()
p1.hit_it(p2)
print("HP", p2.hp)
print("HP", p1.hp)
p2.othil()
print("Mana", p2.mana)
print("HP", p2.hp)
print("HP", p1.hp)
p3 = Medvedev("Медведев")
p3.hi()
p3.expremier()