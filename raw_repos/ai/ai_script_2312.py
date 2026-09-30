def transpose_matrix(matrix):
    """Function to transpose 2d list matrix"""
    row = len(matrix) 
    col = len(matrix[0]) 
  
    transpose = [[0 for j in range(row)] for i in range(col)] 
  
    for i in range(row): 
        for j in range(col): 
            transpose[j][i] = matrix[i][j] 
  
    for i in range(col): 
        print(transpose[i]) 

if __name__ == '__main__':
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    transpose_matrix(matrix)