def containsDuplicate(arr):
    seen = set()
    for element in arr:
        if element in seen:
            return True
        seen.add(element)
    return False