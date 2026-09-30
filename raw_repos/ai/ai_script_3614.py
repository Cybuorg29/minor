def multiply_array(arr): 
  sum_of_arr = sum(arr)
  for i in range(len(arr)): 
    arr[i] = arr[i] * sum_of_arr 
  return arr