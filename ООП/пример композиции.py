# -*- coding: utf-8 -*-



class Car():
    def __init__(self):
        self.eng = Engine(1.6)
    
    
class Engine():
    def __init__(self, v):
        self.v = v
        
        
car1 = Car()



# Класс Car создает класс Engine