#for part 1 and 2
n = 3

A = [
    [9, 9, 9]
    [9, 9, 9]
    [9, 9, 9]
    ]

b = "yes"

for i in range(n):
    for j in range(n):
        if A[i][j] != A[j][i]:
            b = "no"

print(b)
