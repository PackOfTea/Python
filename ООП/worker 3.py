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


worker1 = Worker("���������", "������")
worker2 = Worker("������", "�������")


print("������ ���������")
print("���:", worker1.getName())
print("�������:", worker1.getSurname())
print("������:", worker1.getRate(int(input("�� ������� ���� ��������: "))))
print("���������� ����:", worker1.getDays(int(input("�� ������� ���� ��������: "))))
print("���������� �����:", worker1.getSalary())
print("\n")
print("������ ���������")
print("���:", worker2.getName())
print("�������:", worker2.getSurname())
print("������:", worker2.getRate(int(input("�� ������� ���� ��������: "))))
print("���������� ����:", worker2.getDays(int(input("�� ������� ���� ��������: "))))
print("���������� �����:", worker2.getSalary())