from random import randint

a = 6
matrix = [[randint(-10, 10) for j in range(a)] for i in range(a)]

for row in matrix:
    print(row)
    
m = [min(row) for row in matrix]
m2 = m.index(min(m))

print(m2)
print('sum: {}'.format(sum(matrix[m2])));
