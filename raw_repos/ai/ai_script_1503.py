def linear_search(array, num):
    for index, element in enumerate(array):
        if element == num:
            return index
    return -1