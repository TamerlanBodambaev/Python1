def diagonal(A):

    n = 3
    
    for col in range(n):
        scol = col
        srow = 0
        while(scol >= 0 and
              srow < n):
            print(A[srow][scol], end = " ")
            scol -= 1
            srow += 1
        print()
        
    for row in range(1, n):
        srow = row
        scol = n - 1
        while(srow < n and
              scol >= 0):
            print(A[srow][scol], end=" ")
            scol -= 1
            srow += 1
        print()
if __name__ == "__main__":

    A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
    diagonal(A)
