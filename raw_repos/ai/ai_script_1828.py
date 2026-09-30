def add_matrices(a, b):
    # create a new empty matrix, use the same dimensions as a and b
    result = [[0 for x in range(len(a[0]))] for y in range(len(a))]

    # iterate over a and b to complete the matrix addition 
    for i in range(len(a)):
        for j in range(len(a[0])):
            result[i][j] = a[i][j] + b[i][j]

    return result