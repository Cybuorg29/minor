def search_list(nums, value):
    for num in nums:
        if num == value:
            return True
    return False

nums = [2, 4, 6, 8, 10]
value = 6

result = search_list(nums, value)
print(result) # Output: True