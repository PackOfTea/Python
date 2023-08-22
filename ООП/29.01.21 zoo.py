class Pot():
    def __init__(self):
        self._vol = 1000
        self._lvl = 0
    def add_water(self, v):
        if (self._lvl + v) < self._vol:
            self._lvl += v
        else:
            self._lvl = self._vol
p = Pot()
p.add_water(500)
p.add_water(500)
#print(p._lvl)

class Animal():
    def hit_self(self):
        self.hp -= self.hit
    def hit_it(self, target):
        target.hp -= self.hit
    
class Zebra(Animal):
    def __init__(self):
        self.hp = 100
        self.speed = 100
        self.hit = 5
        self.mana = 100
    def heal (self):
        self.regen = 30
        if self.mana > 40:
            self.hp += self.regen
            self.mana -= 40
            
            
class Lion(Animal):
    def __init__(self):
        self.hp = 90
        self.speed = 70
        self.hit = 30
        self.mana = 80
    def crit(self):
         if self.hp != 90:
            self.hit = self.hit + self.hit        

z1 = Zebra()
l1 = Lion()

l1.hit_it(z1)
print("HP1: ", z1.hp)
print("HP1: ", l1.hp, "\n")

z1.hit_it(l1)
print("HP2: ", z1.hp)
print("HP2: ", l1.hp, "\n")

l1.hit_it(z1)
print("HP3: ", z1.hp)
print("HP3: ", l1.hp, "\n")