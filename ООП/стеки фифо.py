class Stack():
    def __init__(self, mx):
        self.store = []
        self.mx = mx

    def push(self, it):
        if len(self.store) >= self.mx:
            print("¬€ œ–≈¬€—»À» Ã¿ —»Ã¿À‹Õ€… –¿«Ã≈– —“≈ ¿!!!")
        else:
            self.store.append(it)
        
    def pop(self):
        if len(self.store) > 0:
            res = self.store[0]
            self.store = self.store[1:]
            return res
        else:
            return "—“≈  œ”—“!!!"
        
        
    def show(self):
        return self.store    

s = Stack(9)

s.push(5)
s.push(9)
s.push(3)
s.push(1)
s.push(5)
s.push(9)
s.push(3)
s.push(1)
s.push(5)
s.push(9)

print(s.show())

print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())

print(s.show())

print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())

print(s.show())