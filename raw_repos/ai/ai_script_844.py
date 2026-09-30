def flatten_2d_array(arr):
    flat_arr = []
    for subarr in arr:
        flat_arr += subarr
    return flat_arr

# Driver code
input_list = [[1, 2], [3, 4]]
print(flatten_2d_array(input_list))