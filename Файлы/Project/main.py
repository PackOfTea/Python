import libs.helpers as hlp

import authe.login_and_pass as atr

def vvod():
	login = str(input("Введите логин: "))
	pas = str(input("Введите пароль: "))
	return atr.auth(login,pas)

a = vvod()

com= ""
while a != "n":
	if a == "y":
		com= ""
		while com != "exit":
			com = str(input("какую команду выполнить? "))
			if com == "read":
				print(hlp.ReadData())
					#com = str(input("РљР°РєСѓСЋ РєРѕРјР°РЅРґСѓ РІС‹РїРѕР»РЅРёС‚СЊ? "))
			elif com == "add":
				text = str(input("какие данные добавить? "))
				hlp.AddData(text)
				#com = str(input("РљР°РєСѓСЋ РєРѕРјР°РЅРґСѓ РІС‹РїРѕР»РЅРёС‚СЊ? "))
			elif com == "clear":
				hlp.Clear()
				#com = str(input("РљР°РєСѓСЋ РєРѕРјР°РЅРґСѓ РІС‹РїРѕР»РЅРёС‚СЊ? "))
			elif com == "exit":
				print("вы вышли из программы")
			else:
				print("введите одну из данных команд - \"read\", \"add\", \"clear\", \"exit\"")
				#com = str(input("РљР°РєСѓСЋ РєРѕРјР°РЅРґСѓ РІС‹РїРѕР»РЅРёС‚СЊ? "))
		a = "n"
	else:
		print("vvedi dannie normalno" + "\n")
		vvod()
 
