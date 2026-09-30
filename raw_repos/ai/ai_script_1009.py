def find_max_element(arr):
    """This function takes an array and returns the maximum element"""
    max_el = arr[0]
    for el in arr:
        if el > max_el:
            max_el = el
    return max_el