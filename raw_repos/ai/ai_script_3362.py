def normalize_array(arr):
  # Check if the array is empty
  if len(arr) == 0:
    return []
  
  # Get min and max of the array
  min_el = min(arr)
  max_el = max(arr)
  
  # Normalize elements in the array
  normalized_arr = [(el - min_el) / (max_el - min_el) for el in arr]
  
  return normalized_arr
  
normalized_arr = normalize_array(arr)
print("Normalized array:", normalized_arr)