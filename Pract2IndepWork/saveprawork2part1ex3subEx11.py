import math
x = float(input('enter the variable x:'))
y = int(input('enter the variable y:'))

S = (math.asin(math.pow(x,3))-6)/(8*(math.cos(4*y)-math.sin(4*x)))
print("z={0:.2f}".format(S))
