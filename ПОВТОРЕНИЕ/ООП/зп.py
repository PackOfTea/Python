class Worker():
    def __init__(self, n, sn, r, d):
        self.name = n
        self.surname = sn
        self.rate = r
        self.days = d
        
    def getSalary(self):
        return self.rate * self.days
    
    
    
r1 = Worker("����", "������", 0.8, 30)
r2 = Worker("������", "�������", 1, 21)
r3 = Worker("�����", "��������", 0.6, 0)
r4 = Worker("����", "��������", 0.5, 30)
r5 = Worker("�������", "���������", 0.9, 20)

print(r1.getSalary(), "����� ������")
print(r2.getSalary(), "����� ������")
print(r3.getSalary(), "����� ������")
print(r4.getSalary(), "����� ������")
print(r5.getSalary(), "����� ������")