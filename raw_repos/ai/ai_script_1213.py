def sum_numbers(lst): 
    sum = 0
    for item in lst: 
        if type(item) == int or type(item) == float: 
            sum += item 
    return sum