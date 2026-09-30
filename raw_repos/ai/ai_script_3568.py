# Suggest a code that takes a two-dimensional array as input and flattens it
def flatten_array(arr):
    # Initialize the result array
    result_arr = []

    # Iterate the input array
    for subarr in arr:
        # Iterate each sub-array and add each element to the result array
        for elem in subarr:
            result_arr.append(elem)
    
    # Return the result
    return result_arr