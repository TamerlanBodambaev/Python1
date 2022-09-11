import math
x = int(input('enter the variable x:'))
y = float(input('enter the variable y:'))
z = float(input('enter the variable z:'))
S = (math.fabs(1/math.tan(y+6))**(1/3)) + (math.sqrt(((x+1)** 3) / (4*y - 2*z))) 
print("z={0:.2f}".format(S))
