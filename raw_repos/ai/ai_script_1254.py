def remove_duplicate_integers(nums):
    new_list = []
    for num in nums:
        if num not in new_list:
            new_list.append(num)
    return new_list

print(remove_duplicate_integers([3, 6, 8, 10, 10, 11, 15, 15, 15]))