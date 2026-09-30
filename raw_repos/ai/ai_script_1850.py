def reverse_matrix(matrix):
    """Reverse the order of the rows and columns in a matrix of numbers."""
    reversed_matrix = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            reversed_matrix[j][i] = matrix[i][j]
    return reversed_matrix