def mergeSortedSubarrays(ar1, ar2): 
    # if ar1 is empty 
    if len(ar1) == 0: 
        return ar2   
    # if ar2 is empty 
    if len(ar2) == 0: 
        return ar1 
  
    # compare the first elements of each array
    if ar1[0] < ar2[0]: 
        # add the smaller element to the result
        result = [ar1[0]] 
        # remove the element from the first array 
        ar1.remove(ar1[0]) 
    else: 
        result = [ar2[0]] 
        ar2.remove(ar2[0]) 
  
    # call the same function over the remaining elements in the both arrays
    result = result + mergeSortedSubarrays(ar1, ar2) 
    return result