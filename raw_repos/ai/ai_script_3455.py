def multiply(A, B): 
    # initialize result matrix 
    rows_A = len(A) 
    cols_A = len(A[0]) 
    rows_B = len(B) 
    cols_B = len(B[0]) 
  
    if cols_A != rows_B: 
        print("Cannot multiply the two matrices. Incorrect dimensions.") 
        return  
    # construct result matrix  
    C = [[0 for row in range(cols_B)] for col in range(rows_A)] 
  
    # iterate through and multiply
    for i in range(rows_A): 
        for j in range(cols_B): 
            for k in range(cols_A): 
                C[i][j] += A[i][k] * B[k][j] 
  
    return C