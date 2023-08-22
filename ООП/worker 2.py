class Worker():
    def __init__(self, nm, snm, rt, d):
        self._name = nm
        self._surname = snm 
        self._rate = rt
        self._days = d
        
    def getName(self):
        return self._name
    
    def getSurname(self):
        return self._surname
    
    def getRate(self):
        return self._rate
    
    def getDays(self):
        return self._days
    
    def getSalary(self):
        self.salary = self._rate * self._days
        return self.salary


worker1 = Worker("Александр", "Зайцев", 10, 31)
worker2 = Worker("Сергей", "Пальцев", 15, 31)


print("Первый сотрудник")
print("Имя:", worker1.getName())
print("Фамилия:", worker1.getSurname())
print("Ставка:", worker1.getRate())
print("Отработано дней:", worker1.getDays())
print("Заработная плата:", worker1.getSalary())
print("\n")
print("Второй сотрудник")
print("Имя:", worker2.getName())
print("Фамилия:", worker2.getSurname())
print("Ставка:", worker2.getRate())
print("Отработано дней:", worker2.getDays())
print("Заработная плата:", worker2.getSalary())