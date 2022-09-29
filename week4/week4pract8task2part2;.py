n = 3
k = 4

ar = [
    [1, 2, 3, 4]
    [5, 6, 7, 8]
    [9,10,11,12]
    ]

for i in range(n):
    t = ar[i][0]
    ar[i][0] = ar[i][k-1]
    ar[i][k-1] = t

for i in range(n):
    for j in range(k):
        print("%2d " % ar[i][j], end='')
print();
