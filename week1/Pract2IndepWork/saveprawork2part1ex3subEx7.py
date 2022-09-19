import math
x = float(input('enter the variable x:'))
y = float(input('enter the variable y:'))
z = int(input('enter the variable z:'))
S = math.sqrt((1 - x + (1 / math.atan(x - 7 * y)))/((4 * x * z) - (math.log(y)) ** 2)) ** 5
print("z={0:.2f}".format(S))
