# -*- coding: utf-8 -*-

class Cat():
    def __init__(self):
        self.hp = 100
        self.sword = None
        self.dmg = 10
        self.step = 3
        self.point = 0
    
    def takeSword(self, sw):
        if self.sword:
            self.sword = sw
    
    def attack(self, enemy):
        if self.sword:
            enemy.hp -= (self.dmg + self.sword.dmg)
        else:
            enemy.hp -= self.dmg
            
    def go(self):
        self.point += self.step
        if self.point >= 20:
            self.sword = True
        
class Sword():
    def __init__(self):
        self.dmg = 10
        
        
                
c1 = Cat()
c2 = Cat()
sw = Sword()
c1.attack(c2)
c2.go()
c2.go()
c2.go()
c2.go()
c2.go()
c2.go()
c2.go()



print(c2.point)
c2.takeSword(sw)
c2.attack(c1)
print (c1.hp)
print (c2.hp)