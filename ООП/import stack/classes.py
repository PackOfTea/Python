# -*- coding: utf-8 -*-

class Stack():
    def __init__(self, mx):
        self.store = []
        self.mx = mx
        
    def show(self):
        return self.store
    
    def front(self):
        return self.store[0]
    
    def back(self):
        return self.store[-1]
    
    def size(self):
        return len(self.store)
    
    def clear(self):
        self.store = []

class Filo(Stack):
    def push(self, it):
        if len(self.store) >= self.mx:
            print("ВЫ ПРЕВЫСИЛИ МАКСИМАЛЬНЫЙ РАЗМЕР СТЕКА!!!")
        else:
            self.store.append(it)
        
    def pop(self):
        if len(self.store) > 0:
            res = self.store[-1]
            self.store = self.store[:-1]
            return res
        else:
            return "СТЕК ПУСТ!!!"
    
class Fifo(Stack):
    def push(self, it):
        if len(self.store) >= self.mx:
            return "ВЫ ПРЕВЫСИЛИ МАКСИМАЛЬНЫЙ РАЗМЕР СТЕКА!!!"
        else:
            self.store.append(it)
        
    def pop(self):
        if len(self.store) > 0:
            res = self.store[0]
            self.store = self.store[1:]
            return res
        else:
            return "СТЕК ПУСТ!!!"