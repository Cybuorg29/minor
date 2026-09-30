def intersection(arr1, arr2): 

    result = []
    
    i = 0
    j = 0
  
    while i < len(arr1) and j < len(arr2): 
        if arr1[i] < arr2[j]: 
            i += 1
        elif arr2[j] < arr1[i]: 
            j += 1
        else: 
            result.append(arr2[j]) 
            j += 1
            i += 1
  
    return result