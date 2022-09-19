import math
x = int(input('enter the variable x:'))
y = int(input('enter the variable y:'))
z = int(input('enter the variable z:'))
S = (4 * math.fabs(x) - x * y *((z) ** 2)) / (x + math.exp(y * x) - 2 * y * z)
print("z={0:.2f}".format(S))
