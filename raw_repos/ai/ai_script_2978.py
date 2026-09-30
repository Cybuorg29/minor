def is_subset(a, b): 
    for i in a: 
        if i not in b: 
            return False 
    return True