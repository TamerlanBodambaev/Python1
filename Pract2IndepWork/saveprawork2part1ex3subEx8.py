import math
x = float(input('enter the variable x:'))
y = float(input('enter the variable y:'))
z = int(input('enter the variable z:'))
S = ((2*3*4) / (math.pow(math.sin(x),3)+math.pow(math.tan(y),3))) - math.sqrt(math.pow(z,(x-y)))
print("z={0:.2f}".format(S))
