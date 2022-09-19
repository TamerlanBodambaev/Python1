import math
x = int(input('enter the variable x:'))

S = (math.pow(math.log(x-3),4) + math.pow(2,x) * math.pow(math.sin(3*x),2)) / (4*x-5.2)
print("z={0:.2f}".format(S))
