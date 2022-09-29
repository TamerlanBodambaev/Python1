#for part 1 and 2
ar = [[-9, -8, -7, 7],
      [-7, -6, -5, -5],
      [-5, -4, -3, -3],
      [3, -2, -1, 0]]

for i in ar :
    print(*map('{:2d}'.format, i))
print()

n = 4
arr = list(map(list,zip(*ar)))

for i in range(n) :
    for j in range(n) :
        if ar[i] == arr[j] :
            print(i + 1, 'string and ', j + 1, 'the column is equal');
