def subsetsum(arr, target):
  arr.sort() 
  n = len(arr) 
  sum = 0
  result = [] 
  
  for i in range(n):
    if ( sum + arr[i] <= target):
      result.append(arr[i])
      sum = sum + arr[i]
  
  return result