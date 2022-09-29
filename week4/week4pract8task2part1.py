n = 3
ar = [
    [2, 7, 6]
    [9, 5, 1]
    [4, 3, 8]
    ]
S = 0

for i in range(n):
    S += ar[0][i]
    t = "yes"
for i in range(N):
    S1 = 0
    S2 = 0
for j in range(N):
    S1 += ar[i][j]
    S2 += ar[j][i]
if S1 != S or S2 != S:
    t = "no"

print(t)
