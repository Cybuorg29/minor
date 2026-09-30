def element_frequency(arr):
    # use a dictionary to store the frequency of each element
    frequency = {}

    # loop through the list and keep a count of each element
    for elem in arr:
        if elem in frequency:
            frequency[elem] += 1
        else:
            frequency[elem] = 1

    return frequency