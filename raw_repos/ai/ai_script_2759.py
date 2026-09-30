def print_in_spiral_order(arr):
    row_start = 0
    row_stop = len(arr) - 1
    col_start = 0 
    col_stop = len(arr[0]) - 1
    while row_start <= row_stop and col_start <= col_stop:
        for i in range(col_start, col_stop + 1):
            print(arr[row_start][i], end=' ')
        row_start += 1
        for i in range(row_start, row_stop + 1):
            print(arr[i][col_stop], end=' ')
        col_stop -= 1
        if row_start <= row_stop:
            for i in range(col_stop, col_start - 1, -1):
                print(arr[row_stop][i], end=' ')
        row_stop -= 1
        if col_start <= col_stop:
            for i in range(row_stop, row_start - 1, -1):
                print(arr[i][col_start], end=' ')
        col_start += 1