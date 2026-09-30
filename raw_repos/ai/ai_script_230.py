def find_max_sum(arr, k):
    max_sum = 0
    window_sum = 0
    
    # Compute the sum of first k elements 
    for i in range(k):
        window_sum += arr[i]
        
    max_sum = window_sum
    
    # Add new element while removing the first
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
        
    return max_sum