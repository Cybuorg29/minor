def add_matrices(matrix1, matrix2):
    # assert that the matrices are of equal size
    assert len(matrix1) == len(matrix2), "Matrices should have the same size"
    assert len(matrix1[0]) == len(matrix2[0]), "Matrices should have the same size"

    # add the elements
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            matrix1[i][j] += matrix2[i][j]

    return matrix1