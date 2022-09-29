n = 3
k = 4

ar = [
    [12,11,9,10]
    [8, 7, 6, 5]
    [4, 3, 2, 1]
    ]


for i in range(n):
    imin = 0
    iimin = ar[i][0]
    for j in range(k):
        if ar[i][j] < iimin:
            imin = j
            iimin = ar[i][j]
            t = ar[i][0]
ar[i][0] = ar[i][imin]
ar[i][imin] = t

for i in range(n):
    imax = 0
    iimax = ar[i][0]
    for j in range(k):
        if ar[i][j] > iimax:
            imax = j
            iimax = ar[i][j]
            t = ar[i][k-1]
ar[i][k-1] = ar[i][imax]
ar[i][imax] = t

for i in range(n):
    for j in range(k):
        print("%2d " % ar[i][j], end='')
print()
