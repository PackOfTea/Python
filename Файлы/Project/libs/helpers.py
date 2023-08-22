def ReadData():
	file = open("Store.txt", "r")
	data = file.read()
	file.close()
	return data


def AddData(st):
	file = open("Store.txt", "a")
	file.write(st + "\n")
	file.close()
	
def Clear():
	file = open("Store.txt", "w")
	file.write("")
	file.close()
