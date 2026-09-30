def generate_identity_matrix():
    matrix = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == j:
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0
    
    return matrix