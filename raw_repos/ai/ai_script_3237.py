def get_mismatches(arr1, arr2):
    mismatches = 0
    if len(arr1) != len(arr2):
        return -1
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            mismatches += 1
    return mismatches