def rearrange_string(my_str):
    arr = list(my_str)
    i, j = 0, 1
    while i < len(arr):
        if i+1 < len(arr) and arr[i] == arr[i+1]:
            while j < len(arr):
                if arr[j] != arr[i]:
                    arr[i+1], arr[j] = arr[j], arr[i+1]
                    break
                j += 1
        i += 1
    return "".join(arr)