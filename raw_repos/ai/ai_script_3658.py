arr = [1, 1, 2, 3, 3, 3, 4, 5]

def count_number(arr, num):
    count = 0
    for val in arr:
        if val == num:
            count += 1
    return count

count = count_number(arr, 3)
print(count)  # Output: 3