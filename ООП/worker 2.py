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


worker1 = Worker("���������", "������", 10, 31)
worker2 = Worker("������", "�������", 15, 31)


print("������ ���������")
print("���:", worker1.getName())
print("�������:", worker1.getSurname())
print("������:", worker1.getRate())
print("���������� ����:", worker1.getDays())
print("���������� �����:", worker1.getSalary())
print("\n")
print("������ ���������")
print("���:", worker2.getName())
print("�������:", worker2.getSurname())
print("������:", worker2.getRate())
print("���������� ����:", worker2.getDays())
print("���������� �����:", worker2.getSalary())