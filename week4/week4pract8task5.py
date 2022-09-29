#for part 1 and 2
from random import randint

n, k = 4, 3
l = [[randint(-50, 50) for _ in range(k)] for _ in range(n)]
print(list([(1 if min(i) % 2 else 0) if j == min(i) else j for j in i] for i in l))
