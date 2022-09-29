#for part 1 and 2
import numb as np

n = 10
a = np.random.randint(n)
b = np.random.randint(10, 100, size=(n, n))
print(b)
for i in range(0, len(b)):
    print(b[a, i], '/', a[i, i], '=',  b[a, i] / b[i, i])
