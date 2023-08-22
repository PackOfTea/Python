# вводитс€ сторка слов, разделенных пробелами
# определить длину самого короткого слова

# -*- coding: utf-8 -*-
print("приветствуем теб€ в Ѕыдлостане. чувствуй себ€ как в тюр€чке")



cod = 0
simv = 0
minn = 5000
b = True
while b == True:
    stroka = input("вводи строку олень: ")
    if stroka[0] != " ":
        for i in range (0,len(stroka),1):
            cod = ord(stroka[i])
            if cod != 32:
                simv += 1
            else:
                if minn > simv:
                    minn = simv
                    simv  = 0
                    b = False
        if minn == 5000:
            print("“”“ Ќ≈“ ѕ–ќЅ≈Ћќ¬ јјјјјјјјјјјјјјјјјјјјј")
            simv = 0
    else:
        print("ты дурак и ввел в начале строки пробел, дебил. вводи заново, лол")
        simv = 0

#minn = simv
print(minn)