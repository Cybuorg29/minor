def find_index(arr, val):
    for index, elem in enumerate(arr):
        if val == elem:
            return index
    return -1

print(find_index([1, 2, 3, 4], 3))
# Output: 2