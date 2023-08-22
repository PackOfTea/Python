s = str(input())
x = 0
n = 0
p = 0
pp = 0
mx = 0
gl = 0
sgl = 0
for i in range(len(s)):
    if s[i] == "p":
        p += 1

for i in range(len(s)):
    if s[i] == "p":
        x = 0
        n += 1
        pp += 1
    elif s[i] != "p":
        x += 1
        if n == 0:
            x = 0
        if pp == p:
            x = 0
        if mx < x:
            mx = x


    if s[i] == "a" or s[i] == "e" or s[i] == "i" or s[i] == "o" or s[i] == "u" or s[i] == "y":
        gl += 1
    else:
        sgl += 1


print("максимальное расстояние - ", mx)
print("количество гласных - ", gl)
print("количество согласных - ", sgl)
