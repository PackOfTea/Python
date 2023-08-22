arr = [[545, 561, 510, 518, 560],
       [869, 666, 849, 846, 846],
       [752, 885, 555, 635, 123],
       [225, 855, 545, 532, 524],
       [465, 456, 846, 496, 459]
       ]

summ = 0
for i in range (0, len(arr), 1):
    for j in range (0, len(arr), 1):
        summ = summ + arr[i][j]

print(summ)