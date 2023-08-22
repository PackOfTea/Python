# -*- coding: utf-8

class FileDB():
    def __init__(self, fn):
        self.fName = fn
        
    def read(self):
        with open(self.fName, "r") as f:
            data = f.read()
        return data
    
    def readLines(self, tekst):
        tekst.split("\n")
        
    def adder(self, st):
        with open(self.fName, "a") as f:
            f.write(st + "\n")
            
    def clear(self):
        with open(self.fName, "w") as f:
            f.write("")