class Worker():
    def __init__(self, nm, snm):
        self.name = nm
        self.surname = snm 
        self.rate = 10
        self.days = 31
        
    def getName(self):
        return self.name
    
    def getSurname(self):
        return self.surname
    
    def getRate(self, reg):
        self.rate += reg
        return self.rate
    
    def getDays(self, days):
        self.days += days
        return self.days
    
    def getSalary(self):
        self.salary = self.rate * self.days
        return self.salary


worker1 = Worker("Александр", "Зайцев")
worker2 = Worker("Сергей", "Пальцев")


print("Первый сотрудник")
print("Имя:", worker1.getName())
print("Фамилия:", worker1.getSurname())
print("Ставка:", worker1.getRate(int(input("На сколько надо изменить: "))))
print("Отработано дней:", worker1.getDays(int(input("На сколько надо изменить: "))))
print("Заработная плата:", worker1.getSalary())
print("\n")
print("Второй сотрудник")
print("Имя:", worker2.getName())
print("Фамилия:", worker2.getSurname())
print("Ставка:", worker2.getRate(int(input("На сколько надо изменить: "))))
print("Отработано дней:", worker2.getDays(int(input("На сколько надо изменить: "))))
print("Заработная плата:", worker2.getSalary())