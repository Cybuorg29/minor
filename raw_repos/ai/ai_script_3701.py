def transpose(matrix):
    tr_matrix = [[None for i in range(len(matrix))] for j in range(len(matrix[0]))]
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            tr_matrix[j][i] = col
    return tr_matrix