def multiply(m1, m2, n):
    result = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += m1[i][k] * m2[k][j]
    return result