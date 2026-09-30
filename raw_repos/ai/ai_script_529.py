def long_increasing_subsequence(arr):
    # Number of items in given array
    n = len(arr)
 
    # Initialize 'lengths' values for all indices
    lengths = [1]*n
 
    # Find the longest increasing subsequence
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i] and lengths[j] + 1 > lengths[i]:
                lengths[i] = lengths[j] + 1
 
    return lengths