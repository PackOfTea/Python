# �������� ������ ����, ����������� ���������
# ���������� ����� ������ ��������� �����

# -*- coding: utf-8 -*-
print("������������ ���� � ����������. �������� ���� ��� � �������")



cod = 0
simv = 0
minn = 5000
b = True
while b == True:
    stroka = input("����� ������ �����: ")
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
            print("��� ��� �������� ���������������������")
            simv = 0
    else:
        print("�� ����� � ���� � ������ ������ ������, �����. ����� ������, ���")
        simv = 0

#minn = simv
print(minn)