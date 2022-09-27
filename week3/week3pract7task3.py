import math
ca = int(input('Enter: '))
cb = int(input('Enter: '))
cc = int(input('Enter: '))
cd = int(input('Enter: '))

hx = float(math.sqrt(ca*ca + cb*cb))
hy = float(math.sqrt(cc*cc + cd*cd))
print(hx)

if hx > hy:
    xy = hx - hy
    print('hypotenuse x > hypotenuse y by: ' + str(xy) + '.\nhypotenuse x: ' + str(hx) + '.\nhypotenuse y: ' + str(hy))
else:
    yx = hy - hx
    print('The hypotenuse y > hypotenuse x by: ' + str(yx) + '.\nhypotenuse x: ' + str(hx) + '.\nhypotenuse y: ' + str(hy))
