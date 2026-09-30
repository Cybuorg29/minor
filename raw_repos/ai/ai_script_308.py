def create_list(start, end, step): 
    list = [] 
    while start < end: 
        list.append(start) 
        start += step 
    return list