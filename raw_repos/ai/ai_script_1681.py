def reorder_arr(arr): 
  negatives = [] 
  positives = [] 

  for item in arr: 
    if item < 0: 
      negatives.append(item) 
    elif item >= 0: 
      positives.append(item) 
    
  return negatives + positives