def sort_numbers_desc(arr): 
    for i in range(len(arr)): 
  
        max_element = arr[i] 
        max_index = i 
  
        for j in range(i+1, len(arr)): 
            if arr[j] > max_element: 
                max_element = arr[j] 
                max_index = j  
  
        arr[i], arr[max_index] = arr[max_index], arr[i] 
    return arr

print(sort_numbers_desc(arr))