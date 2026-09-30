def find_max(arr):
    max = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max

arr = [7, 9, -2, 15, 3]
print(find_max(arr))