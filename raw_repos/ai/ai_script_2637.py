def recursive_sum(lst): 
    # Base case
    if not len(lst): 
        return 0
    return lst[0] + recursive_sum(lst[1:])