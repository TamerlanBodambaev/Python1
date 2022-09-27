A = 1 
B = 3 
C = 1
D = 5

l = A * D + B * C
k = B * D

x, y = l, k
while x != y:
    if A > B:
        x -= y
    else:
        y -= x
print (f'{l // x}/{k // A}')
