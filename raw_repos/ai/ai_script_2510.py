def search_list(nums, target):
    """
    Function to search a list of integers and print the index of the first matched item 
    """
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

print(search_list([4, 7, 1, 2, 5], 7))