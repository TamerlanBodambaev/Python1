matrix = [[]] 
diagonal = []

for j in range(len(matrix)):
    diagonal.append(matrix[j][j])

print(diagonal)
print(sum(diagonal))
