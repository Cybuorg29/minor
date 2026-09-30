def max_sum_path(matrix):
    rows, columns = len(matrix), len(matrix[0])
    dp = [[float("-inf") for i in range(columns)] for j in range(rows)]
    dp[0][0] = matrix[0][0]
    for i in range(rows):
        for j in range(columns):
            if i > 0:
                dp[i][j] = max(dp[i][j], dp[i-1][j] + matrix[i][j])
            if j > 0:
                dp[i][j] = max(dp[i][j], dp[i][j-1] + matrix[i][j])
    return dp[-1][-1]