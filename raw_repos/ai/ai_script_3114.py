def find_duplicate(arr):
    seen = set()
    for item in arr:
        if item in seen:
            return item
        else:
            seen.add(item)
    return None # if no duplicate

find_duplicate(arr) # Returns 2