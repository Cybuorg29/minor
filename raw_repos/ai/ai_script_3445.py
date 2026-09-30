import numpy as np

# Create the matrix
matrix = np.array([[0, 1, 2], 
                   [3, 4, 5], 
                   [6, 7, 8]])

# Get the lengths of each row
row_lengths = [len(row) for row in matrix]

# Delete the row with the minimum length and print the result
del matrix[row_lengths.index(min(row_lengths))]
print(matrix) # prints [[0 1 2] 
                  #        [3 4 5] 
                  #        [6 7 8]]