#�� -20 �� 25 ��������� ����� � ������  m*n yf 'rhfy

import random



m = int(input("����� �������"))
n = int(input("������ �������"))

arr = []

for i in range (0, m, 1):
    arr_r = []
    for j in range (0, n, 1):
        arr_r.append(random.randint(-20,25))
    arr.append(arr_r)
    

print(arr)