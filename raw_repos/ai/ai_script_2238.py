def search(items, item): 
    for i in range(len(items)): 
    if items[i] == item:
        found = i 
    if found: 
        return found 
    else: 
        return -1