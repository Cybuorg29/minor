def transpose_matrix(matrix):
    transposedMatrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0])) ]
    return transposedMatrix

transposedMatrix = transpose_matrix(matrix)
print(transposedMatrix)