class Worker():
    def __init__(self, n, sn, r, d):
        self.name = n
        self.surname = sn
        self.rate = r
        self.days = d
        
    def getSalary(self):
        return self.rate * self.days
    
    
    
r1 = Worker("Иван", "Петров", 0.8, 30)
r2 = Worker("Андрей", "Сидоров", 1, 21)
r3 = Worker("Роман", "Кокшаров", 0.6, 0)
r4 = Worker("Иван", "Варламов", 0.5, 30)
r5 = Worker("Алексей", "Навальный", 0.9, 20)

print(r1.getSalary(), "тысяч рублей")
print(r2.getSalary(), "тысяч рублей")
print(r3.getSalary(), "тысяч рублей")
print(r4.getSalary(), "тысяч рублей")
print(r5.getSalary(), "тысяч рублей")