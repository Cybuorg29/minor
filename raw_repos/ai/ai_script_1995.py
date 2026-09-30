def flatten(arr):
    flat_list = []
    for sublist in arr:
        for item in sublist:
            flat_list.append(item)
    return flat_list