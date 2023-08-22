# -*- coding: utf-8 -*-

class Politpet():
    def hi(self):
        print("Салам, я " + self.breed + " " + self.nm)


class Medvedev(Politpet):
    def __init__(self, name):
        self.hp = 100
        self.hit = 300
        self.mana = 200
        self.breed = "Димон"
        self.nm = name
    def hi(self):
        print ("Денег нет, но вы держитесь")   

p1 = Medvedev("Медведев")
p1.hi()