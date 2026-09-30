def insertion_sort_reverse(arr):
    """ Sort the list in reverse order using insertion sort. """
    # Iterate over the list
    for i in range(1, len(arr)):
        current_value = arr[i]
        # Keep track of position
        position = i
        # Iterate over the sorted part of the list
        while position > 0 and arr[position - 1] < current_value:
            # Shift one place to the right
            arr[position] = arr[position - 1]
            # Move position back
            position = position - 1
        # Insert current value at the position
        arr[position] = current_value
    return arr

insertion_sort_reverse([4, 2, 0, 6, 1, 7, 3]) # Outputs[7, 6, 4, 3, 2, 1, 0]