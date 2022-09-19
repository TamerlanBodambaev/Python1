import math
x = int(input('enter the variable x:'))
y = float(input('enter the variable y:'))

S = ((5 * x * y) / (math.pow(x,3) - 4)) + (math.exp(math.pow(x,2))) + (math.sqrt((math.cos(y) ** 2) - math.pow(y,2)))
print("z={0:.2f}".format(S))
