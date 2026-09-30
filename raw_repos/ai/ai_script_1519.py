def remove_duplicates(arr):
    """Remove the duplicates from the list without using built-in methods."""
    # Initialize empty list
    new_list = []
    # Iterate through array
    for num in arr:
        # Check if element is not in list
        if num not in new_list:
            # Add element to list
            new_list.append(num)
    return new_list

remove_duplicates([1, 2, 1, 2, 3, 2, 4, 2]) # Outputs [1, 2, 3, 4]