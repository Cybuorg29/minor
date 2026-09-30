def find_most_frequent_element(arr):
    d = {}
    for num in arr:
        if num in d: 
            d[num] += 1
        else:
            d[num] = 1
    
    max_freq = 0
    most_frequent_element = None
    for num in d:
        if d[num] > max_freq:
            max_freq = d[num]
            most_frequent_element = num

    return most_frequent_element