def adjacent_elements_count(arr):
    count = 0
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            count += 1

    return count

print(adjacent_elements_count(a))