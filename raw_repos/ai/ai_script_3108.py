def binary_search(my_array, x): 
    start = 0
    end = len(my_array) - 1
  
    while start <= end: 
  
        mid = (start + end) // 2 # calculate mid
  
        # Check if x is present at mid 
        if my_array[mid] < x: 
            start = mid + 1
  
        # If x is greater, ignore left half 
        elif my_array[mid] > x: 
            end = mid - 1
  
        # If x is smaller, ignore right half 
        else: 
            return mid 
    # If we reach here, then the element 
    # was not present 
    return -1