import numpy as np


def printMatrix(matrix):
    for i in range(3):
        print(str(matrix.item(i*3)) + " " + str(matrix.item(i*3 + 1)) + " " + str(matrix.item(i*3 + 2)))

mat = np.matrix([[0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0]])
# number 1
for i in range(3):
    mat[i,i] = 1
printMatrix(mat)
print()

# number 2
for i in range(3):
    for j in range(3):
        if i != j:
            mat[i,j] += 3
printMatrix(mat)
print()

# number 3
mat = np.delete(mat, 2, 1)
for i in range(3):
    print(str(mat[i,0]) + " " + str(mat[i,1]))
        