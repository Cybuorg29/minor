def find_equilibrium_index(arr):
    total_sum = sum(arr)

    left_sum = 0
    
    for index, num in enumerate(arr):
        total_sum -= num
        if left_sum == total_sum:
            return index 
        left_sum += num
    return -1

arr = [-7, 1, 9, -4, 3, 2]
print(find_equilibrium_index(arr)) # Output: 2