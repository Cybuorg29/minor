def sort_array(arr): 
  # Loop through the array, swap each element until it is in order (ascending)
  for i in range(len(arr) - 1): 
    for j in range(i + 1, len(arr)): 
      if arr[i] > arr[j]: 
        temp = arr[i] 
        arr[i] = arr[j] 
        arr[j] = temp 
  
  # Return the sorted array 
  return arr

print(sort_array(arr)) # [1, 3, 4, 5, 12, 85]