class Book():
	def __init__(self, nm, avt, g, lit, vozrast):
		self.name = nm
		self.autor = avt
		self.year = g
		self.vid = lit
		self.age = vozrast

class Library():
	def __init__(self):
		self.libra = []
	
	def addBook(self, book):
		self.libra.append(book)
		
	def getBooksByAuth(self, auth):
		arr = []
		for b in self.libra:
			if b.autor == auth:
				arr.append(b.name)
			
		if arr == []:
			return "��� ������ ������"
			
		return arr
			
	def showBookList(self):
		for b in self.libra:
			print(b.name, b.autor, b.year, b.vid, b.age)

b1 = Book("������� � ��������", "���� ���", "2021", "��������������", "+88")
b2 = Book("����������� ��", "��", "2020", "����������", "+0")
b3 = Book("������������ � ���������", "�������", "1920", "��������������", "+0")
b4 = Book("����� � ���", "�������", "1960", "��������������", "+18")
b5 = Book("�UM������", "���� ���", "2021", "�������", "+0")
l = Library()
l.addBook(b1)
l.addBook(b2)
l.addBook(b3)
l.addBook(b4)
l.addBook(b5)
l.showBookList()
print(l.getBooksByAuth(input("vvedi avtora ")))
