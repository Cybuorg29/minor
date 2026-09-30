def matrix_dimensions(matrix):
    num_rows = len(matrix)
    num_columns = len(matrix[0])
    return num_rows, num_columns

matrix = [[1, 2, 3, 4], 
          [5, 6, 7, 8], 
          [9, 10, 11, 12]]

num_rows, num_columns = matrix_dimensions(matrix)
print(num_rows) # Output will be 3
print(num_columns) # Output will be 4