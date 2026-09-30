def shift_left(arr): 
    # Shifting the array elements from position 1 to n-1 
    for i in range(1, len(arr)): 
        arr[i - 1] = arr[i] 
  
    # Replacing the last element with 0 
    arr[len(arr) - 1] = 0
    return arr