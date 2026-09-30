def sum_elements(X):
    sums = 0
    for i in range(len(X)):
        for j in range(len(X[i])):
            sums+=X[i][j]
    return sums

print(sum_elements(X))