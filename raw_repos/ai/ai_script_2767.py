def filter_strings(arr):
 filtered_arr = [s for s in arr if len(s) <= 5]
 return filtered_arr
  
print(filter_strings(arr)) # Prints ["code", "Loops"]