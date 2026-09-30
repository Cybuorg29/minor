def max_subarray_sum(list_of_numbers): 
 
    max_so_far = 0
    max_ending_here = 0
 
    for i in range(0,len(list_of_numbers)): 
        max_ending_here = max_ending_here + list_of_numbers[i] 
        if (max_ending_here < 0): 
            max_ending_here = 0
  
        elif (max_so_far < max_ending_here): 
            max_so_far = max_ending_here 
              
    return max_so_far