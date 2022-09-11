import math
x = int(input('enter the variable x:'))
y = int(input('enter the variable y:'))
z = int(input('enter the variable z:'))
S = math.sqrt(0.6*x*y*z) + math.pow(math.pow(y,x),2) - math.exp(math.sin(2*(x**2)))
print("z={0:.2f}".format(S))
