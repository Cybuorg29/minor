def flatten_list(list):
    s=[]
    
    for v in list:
        if isinstance(v, list):
            s+=flatten_list(v)
        else:
            s.append(v)
    
    return s