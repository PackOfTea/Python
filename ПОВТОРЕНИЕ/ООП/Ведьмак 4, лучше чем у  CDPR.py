# -*- coding: utf-8 -*-

import random

class MagicBook():
    def __init__(self):
        self.extraMana = random.randint(-40,40)
        
class Witch():
    def __init__(self, obj_book):
        self.book = obj_book
        self._mana = 30
        
        
    def getMana(self):
        self._mana += self.book
        
    def setMana(self):
        if self._mana < 5:
            print("Вы проиграли")
            self._mana = 0
        elif self._mana > 65:
            self._mana = 65
            print("У вас максимальное количество маны")
            
class Program():
    def changeMana(self):
        kniga = MagicBook()
        w1 = Witch(kniga)
        w1.getMana()
        w1.setMana()
        print(w1._mana)
        
p = Program()
p.changeMana()