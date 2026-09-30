def get_smallest_largest(arr):
    """
    Function to return the smallest and largest numbers in a list
    Parameters:
        arr: An unsorted list of numbers
    Returns:
        A tuple containing the smallest and largest numbers in the list
    """
    smallest = arr[0]
    largest = arr[0]

    for elem in arr:
        if elem < smallest:
            smallest = elem
        if elem > largest:
            largest = elem
    
    return (smallest, largest)