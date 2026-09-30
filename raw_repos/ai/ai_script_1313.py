def largest_negative_number(arr): 
    largest = float('-inf')
    for i in range(len(arr)): 
        if arr[i] > largest: 
            largest = arr[i] 
    return largest 
  
# Driver Code 
arr = [-10, -20, -50, -30] 
  
print(largest_negative_number(arr))