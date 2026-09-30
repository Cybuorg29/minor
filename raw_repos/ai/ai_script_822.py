def merge_arrays(arr1, arr2):
    # creating a new list to store the result
    merged_arr = []
    # looping over the two arrays
    for i in range(len(arr1)):
        merged_arr.append(arr1[i])
    for i in range(len(arr2)):
        merged_arr.append(arr2[i])
    # sorting function to sort the merged array
    merged_arr.sort()
    return merged_arr

# Driver code
new_arr = merge_arrays(arr1, arr2)

# to print the sorted merged array
print(new_arr)
# Output: [2, 3, 4, 5, 7]