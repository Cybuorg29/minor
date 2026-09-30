def count_unique_elements(arr):
    """Returns the number of unique elements present in the given array."""
    unique_elements = set(arr)
    return len(unique_elements)

if __name__ == '__main__':
    arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    count = count_unique_elements(arr)
    print('Number of unique elements:', count)