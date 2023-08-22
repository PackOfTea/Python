# -*- coding: utf-8 -*-

class Animal():
    def hi(self):
        print("Hi, i am " + self.name)
        
class Hamst(Animal):
    def __init__(self, name):
        self.name = name
        
    def hi(self):
        print("********")
        super().hi()
        print("********")
        
class Toad(Animal):
    def __init__(self, name):
        self.name = name
        
        
t = Toad("Vasa")
h = Hamst("Olehhhhh")

t.hi()
h.hi()