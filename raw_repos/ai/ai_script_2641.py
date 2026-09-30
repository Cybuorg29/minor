def array_sum(arr): 
    total = 0
    # Iterate through arr and add elements to total  
    for i in range (0, len(arr)): 
        total += arr[i] 
    return total 
  
# Driver code 
arr = [2, 4, 7, 10] 
sum = array_sum(arr) 
print (sum) # -> 23