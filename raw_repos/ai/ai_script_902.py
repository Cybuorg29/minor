def min_element(lis):
    # set min to first element in the list
    min = lis[0]
  
    # iterate over the list and compare each element to 
    # the current minimum. If a smaller element is found, 
    # update min. 
    for x in lis:
        if x < min: 
            min = x
  
    # return min
    return min