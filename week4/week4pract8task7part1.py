matrix = [][] 

for i in range(len(matrix)): 
    matrix[i][i] = int(input())

for j in range(i + 1, len(matrix)):
    matrix[i][j] = int(input())
    matrix[j][i] = matrix[i][j]

print(matrix);
