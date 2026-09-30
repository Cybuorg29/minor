def sort_increasing(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

arr = [2, 5, 3, 8, 7] 
sorted_arr = sort_increasing(arr)
print(*sorted_arr) # Output: 2 3 5 7 8