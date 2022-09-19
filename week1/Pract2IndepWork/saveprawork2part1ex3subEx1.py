import math
x = int(input('enter the variable x:'))
y = int(input('enter the variable y:'))

S = math.pow(math.pow(x,y),x)+math.pow(x,math.pow(x,y))-math.pow(x,4)
print("z={0:.2f}".format(S))
