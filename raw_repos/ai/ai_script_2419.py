def rotate_2d_matrix(matrix):
    n = len(matrix[0])
    m = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            m[i][j] = matrix[n-j-1][i]
    return m