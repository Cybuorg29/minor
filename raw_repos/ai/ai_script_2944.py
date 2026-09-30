def remove_duplicates(string):
    res = "" 
    for i in string: 
        if i not in res: 
            res = res + i
    return res