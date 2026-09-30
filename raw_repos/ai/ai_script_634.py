def get_min_max(numbers):
    # Set min and max to first number
    lowest = numbers[0]
    highest = numbers[0]
    # Iterate through each number 
    for num in numbers:
        if num < lowest:
            lowest = num
        if num > highest:
            highest = num
    # Return min and max in a tuple
    return (lowest, highest)

min_max_nums = get_min_max([3, 10, 2, 8, 5])
print(min_max_nums)