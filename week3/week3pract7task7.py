import math

x = float(input('enter X: '))
y = float(input('enter Y: '))
z = float(input('enter Z: '))
t = float(input('enter T: '))

def sq(x, y, z, t):
    a = math.sqrt(x*x+y*y)
    b = x*y*0.5
    c = 0.25*math.sqrt((a+z+t)*(a+z-t)*(a+t-z)*(z+t-a))
    return b + c
