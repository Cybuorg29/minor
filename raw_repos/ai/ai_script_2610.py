def row_sum(A): 
    result = [] 
  
    for row in A: 
        sum = 0  
        for element in row: 
           sum = sum + element 
        result.append(sum) 
  
    return result