def find_max_num(nums_list):
    """This function takes an array and prints out the biggest number in it."""
    max_num = nums_list[0]
    for num in nums_list:
        if num > max_num:
            max_num = num
    return max_num

nums_list = [1, 7, 2, 11, 4]
print(find_max_num(nums_list))