def remove_duplicate(arr):
    newArr = []
    for i in arr:
        if i not in newArr:
            newArr.append(i)
    return newArr