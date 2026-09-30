def greater_than(arr, num):
    result = []
    for el in arr:
        if el > num:
            result.append(el)
    return result

print(greater_than(arr, num))