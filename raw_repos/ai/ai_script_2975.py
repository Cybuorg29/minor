def col_sum(arr):
    col_sum_arr = []
    for j in range(len(arr[0])):
        s = 0
        for i in range(len(arr)):
            s += arr[i][j]
        col_sum_arr.append(s)
    return col_sum_arr

print(col_sum([[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]))
# Output: [12, 15, 18]