import libs.helpers as hlp

import authe.login_and_pass as atr

def vvod():
	login = str(input("������� �����: "))
	pas = str(input("������� ������: "))
	return atr.auth(login,pas)

a = vvod()

com= ""
while a != "n":
	if a == "y":
		com= ""
		while com != "exit":
			com = str(input("����� ������� ���������? "))
			if com == "read":
				print(hlp.ReadData())
					#com = str(input("Какую команду выполнить? "))
			elif com == "add":
				text = str(input("����� ������ ��������? "))
				hlp.AddData(text)
				#com = str(input("Какую команду выполнить? "))
			elif com == "clear":
				hlp.Clear()
				#com = str(input("Какую команду выполнить? "))
			elif com == "exit":
				print("�� ����� �� ���������")
			else:
				print("������� ���� �� ������ ������ - \"read\", \"add\", \"clear\", \"exit\"")
				#com = str(input("Какую команду выполнить? "))
		a = "n"
	else:
		print("vvedi dannie normalno" + "\n")
		vvod()
 
