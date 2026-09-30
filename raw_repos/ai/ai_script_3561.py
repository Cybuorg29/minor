def print_spiral(matrix):
    # matrix is an 2D array 
    row_start = 0
    row_end = len(matrix)-1
    col_start = 0
    col_end = len(matrix[0])-1

    while row_start <= row_end and col_start <= col_end:
        # print top row 
        for i in range(col_start, col_end+1):
            print(matrix[row_start][i])
        # increment row start 
        row_start += 1

        # print right column
        for i in range(row_start, row_end+1):
            print(matrix[i][col_end])
        # decrement col end
        col_end -= 1
        
        # print bottom row
        if row_start <= row_end:
            for i in range(col_end, col_start-1, -1):
                print(matrix[row_end][i])
            # decrement row end
            row_end -= 1

        # print left column
        if col_start <= col_end:
            for i in range(row_end, row_start-1, -1):
                print(matrix[i][col_start])
            # increment col start
            col_start += 1