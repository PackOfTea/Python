class Student():
    def __init__(self, fio, ag, gryppa, dolg):
        self.fios = fio
        self.age = ag
        self.group = gryppa
        self.dolg = dolg

class Teacher():
    def __init__(self, fio, predmet):
        self.fiot = fio
        self.predmet = predmet
    
class Sharaga():
    def __init__(self):
        self.studenti = []
        self.teachers = []
    def addStudent(self, student):
        self.studenti.append(student)
    def showStudentInfo (self):
        for p in self.studenti:
            print(p.fios, p.age, p.group)
    def showStudentByAge(self):
        for p in self.studenti:
            if p.age == 20:
                print(p.fios, p.age, p.group, "���������� ���� � �������...")
    def showStudentByDolgi(self):
        for p in self.studenti:
            if p.dolg == 1:
                print(p.fios, p.age, p.group, "���� ������������� �������������")
        
    def addTeacher(self, teach):
        self.teachers.append(teach)
    def showTeachersInfo(self):
        for t in self.teachers:
            print(t.fiot, t.predmet)
            
            
            
s = Sharaga()
t1 = Teacher("������� ���� �������", "��� ��������")
s1 = Student("��� ���� ���������", 17, "��-11", 1)
s2 = Student("������� ���� �������", 20, "��-11", 0)
s3 = Student("����� ������ ������", 18, "��-11", 1)
s.addStudent(s1)
s.addStudent(s2)
s.addStudent(s3)
s.showStudentInfo()
s.addTeacher(t1)
s.showTeachersInfo()
s.showStudentByAge()
s.showStudentByDolgi()