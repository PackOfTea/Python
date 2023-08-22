file = open("1.txt", "a")
file.write("hello" + "\n")
file.close()

file = open("1.txt", "r")
data = file.read()
file.close()
print(data)
	
