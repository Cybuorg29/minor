def find_max_difference(nums):
    # Initialize a max difference
    max_diff = float('-inf')
    
    # Iterate through the array
    for i in range(1, len(nums)):
        diff = nums[i] - nums[i-1]
        if diff > max_diff:
            max_diff = diff
    
    return max_diff

# Call the function
find_max_difference([3, 2, 7, 1, 4]) # returns 6