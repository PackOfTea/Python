class Worker():
    def __init__(self, nm, snm, rt, d):
        self.name = nm
        self.surname = snm 
        self.rate = rt
        self.days = d
    
    def getSalary(self):
        self.salary = self.rate * self.days
        return self.salary


worker1 = Worker("Александр", "Зайцев", 10, 31)
worker2 = Worker("Сергей", "Пальцев", 15, 31)


print("Первый сотрудник")
print("Имя:", worker1.name)
print("Фамилия:", worker1.surname)
print("Ставка:", worker1.rate)
print("Отработано дней:", worker1.days)
print("Заработная плата:", worker1.getSalary())
print("\n")
print("Второй сотрудник")
print("Имя:", worker2.name)
print("Фамилия:", worker2.surname)
print("Ставка:", worker2.rate)
print("Отработано дней:", worker2.days)
print("Заработная плата:", worker2.getSalary())