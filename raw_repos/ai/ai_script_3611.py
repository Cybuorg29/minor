def sort(array): 
    length = len(array) 
  
    for i in range(length): 
  
        j = i 
        while j > 0 and array[j-1] > array[j]: 
            # Swap elements
            array[j], array[j-1] = array[j-1], array[j] 
            j -= 1

    return array