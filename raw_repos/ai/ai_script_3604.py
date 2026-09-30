def max_min(my_list):
    max_val = my_list[0]
    min_val = my_list[0]

    for val in my_list:
        if val > max_val:
            max_val = val
        
        if val < min_val:
            min_val = val
    
    return (max_val, min_val)