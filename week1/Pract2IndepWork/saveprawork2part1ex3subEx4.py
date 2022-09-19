import math
x = int(input('enter the variable x:'))
y = float(input('enter the variable y:'))

S = (math.sqrt(math.fabs(y)) + ((math.atan(math.log(x)) ** 3) / ( math.pow(x,y) - y + 1) )) 
print("z={0:.2f}".format(S))
