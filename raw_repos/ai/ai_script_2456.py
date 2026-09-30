def reduceArray(arr):
    if not arr:
        return 0
    result = arr[0]
    for num in arr[1:]:
        result = result + num
    return result

print(reduceArray([2, 4, 6, 8, 10])) # Outputs: 30