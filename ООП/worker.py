class Worker():
    def __init__(self, nm, snm, rt, d):
        self.name = nm
        self.surname = snm 
        self.rate = rt
        self.days = d
    
    def getSalary(self):
        self.salary = self.rate * self.days
        return self.salary


worker1 = Worker("���������", "������", 10, 31)
worker2 = Worker("������", "�������", 15, 31)


print("������ ���������")
print("���:", worker1.name)
print("�������:", worker1.surname)
print("������:", worker1.rate)
print("���������� ����:", worker1.days)
print("���������� �����:", worker1.getSalary())
print("\n")
print("������ ���������")
print("���:", worker2.name)
print("�������:", worker2.surname)
print("������:", worker2.rate)
print("���������� ����:", worker2.days)
print("���������� �����:", worker2.getSalary())