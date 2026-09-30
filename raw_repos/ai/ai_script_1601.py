def element_equal(arr, value):
    """Check if any element in the array is equal to the given value."""
    for ele in arr:
        if ele == value:
            return True
    return False