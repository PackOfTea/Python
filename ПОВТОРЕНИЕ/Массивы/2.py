arr = [[545, 561, 510, 518],
       [869, 666, 849, 846],
       [752, 885, 555, 635],
       [225, 855, 545, 532]
       ]

p1 = 0
p2 = 0
p3 = 0
p = 1

for i in range (0, len(arr), 1):
    for j in range (0, len(arr[i]), 1):
        p = p * arr[i][j]
    print(p)
    p = 1