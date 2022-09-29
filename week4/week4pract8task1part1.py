n = 3
ar = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]
cow = 0
S = 0
for i in range(n):
    for j in range(i + 1, n):
        if Ar[i][j] > 0:
            S += ar[i][j]
cow += 1
print("count:",cow)
print("sum:",S)
