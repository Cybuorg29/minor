def reverse_arr(arr):
    """Reverses an array in-place. This means the existing array will be modified!"""
    # reverse the array in-place
    for i in range(len(arr)//2): 
        arr[i], arr[len(arr)-i-1] = arr[len(arr)-i-1], arr[i]