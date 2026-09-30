def get_common_elements(arr1, arr2):
    common_elements = []
    for a in arr1:
        if a in arr2:
            common_elements.append(a)
    return common_elements