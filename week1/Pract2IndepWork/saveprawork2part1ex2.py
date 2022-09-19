import math
x = int(input('enter the variable x:'))
y = int(input('enter the variable y:'))
H = (math.sqrt(math.cos(2*y)+math.sin(4*y) + math.sqrt(math.pow(math.e,x) + math.pow(math.e,(-x)))))/(math.pow(((math.pow(math.e,(-x))) + math.pow(math.e,x)),3) * math.pow((math.sin(4*y) + math.cos(2*y) - 2), 2))
print("z={0:.2f}".format(H))
