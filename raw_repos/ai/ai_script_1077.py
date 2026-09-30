def sort_by_length(arr):
    """
    Sort a list by the reverse order of its length.
    """
    arr.sort(key=len, reverse=True)
    return arr