def pathFinder(matrix, position, n):
    # returns a list of path taken
    if position == (n-1,n-1):
        return [(n-1),(n-1)]
    i,j = position
    # check whether we can move in the right direction
    if i+1 < n and matrix[i+1][j] == 1:
        a = pathFinder(matrix,(i+1,j),n)
        if a != None:
            return [(i,j)]+a

    # check whether we can move in the downward direction
    if j+1 < n and matrix[i][j+1] == 1:
        b = pathFinder(matrix,(i,j+1),n)
        if b != None:
            return [(i,j)]+b


matrix = [[1,1,1,1,0],
          [0,1,0,1,0],
          [0,1,0,1,0],
          [0,0,0,1,0],
          [1,1,1,1,1]]

initialposition = (0,0)
matrixsize = len(matrix)
print(pathFinder(matrix,initialposition,matrixsize))
