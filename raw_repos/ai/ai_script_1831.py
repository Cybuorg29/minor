def recursive_sum(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + recursive_sum(arr[1:])

arr = [1, 3, 7, 9, 11]
print(recursive_sum(arr))