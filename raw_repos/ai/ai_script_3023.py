def min_difference(list1, list2):
    # Initialize the minimum difference to a large number
    min_diff = float('inf')

    for a in list1:
        for b in list2:
            # Update min_diff only if the difference 
            # between a and b is smaller than min_diff 
            min_diff = min(min_diff, abs(a - b))
    
    return min_diff