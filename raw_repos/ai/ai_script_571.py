def reverse_array(arr):
    """
    Construct a new array with the elements reversed.
    """
    new_arr = []
    for i in range(len(arr)-1, -1, -1):
        new_arr.append(arr[i])
    return new_arr