import math
x = float(input('enter the variable x:'))
y = int(input('enter the variable y:'))
z = int(input('enter the variable y:'))
S = ((math.fabs(math.log(x**3))+math.exp(2*x)) / (x+3.4)) - (math.pow(1/math.tan(3/(x*y*z)),3))
print("z={0:.2f}".format(S))
