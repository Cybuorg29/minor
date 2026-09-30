def matrix_multiplication(*matrices):
    res = [[0 for _ in range(len(matrices[0][0]))]
        for _ in range(len(matrices[0]))]
    for y in range(len(matrices[0])):
        for x in range(len(matrices[0][0])):
            for m in range(len(matrices)):
                res[y][x] += matrices[m][y][x]
    return res