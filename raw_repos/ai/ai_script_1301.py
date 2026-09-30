def find_distinct(arr):
    distinct_list = []
    for num in arr:
        if num not in distinct_list:
            distinct_list.append(num)

    return distinct_list

arr = [1, 2, 3, 3, 4, 5]
print(find_distinct(arr))  # Output: [1, 2, 3, 4, 5]