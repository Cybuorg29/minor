def remove_duplicates(arr):
    result = [] 
    for el in arr:
        if el not in result:
            result.append(el)
    return result