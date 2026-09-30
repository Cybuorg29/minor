def longestIncreasingSubarray(arr):
    n = len(arr)
    max_len = 1
    curr_len = 1
    for i in range(1, n): 
     
        #if current element is greater than its previous element 
        if (arr[i] > arr[i-1]):
            curr_len += 1
        else:
            if (curr_len > max_len):
                max_len = curr_len
            curr_len = 1
    #Compare the length of the last 
    #subarray with max_len and 
    #update max_len if needed 
    if (curr_len > max_len):
        max_len = curr_len 
    
    return max_len