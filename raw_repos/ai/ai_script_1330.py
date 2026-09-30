def sublist_sum(numbers, target) : 
    n = len(numbers) 
  
    # Consider all sublists of arr[] and return 
    # true if given sum is present in any of them 
    for i in range(n) : 
        curr_sum = numbers[i] 
  
        # Try different endpoints for current subarray 
        j = i+1
        while j<=n : 
  
            if curr_sum == target : 
                return True
  
            if curr_sum > target or j == n: 
                break
  
            curr_sum = curr_sum + numbers[j] 
            j += 1
  
    return False