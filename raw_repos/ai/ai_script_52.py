def find_min_max(numbers):
    lowest = numbers[0]
    highest = numbers[0]
    for num in numbers:
        if num < lowest:
            lowest = num
        if num > highest:
            highest = num
    return (lowest, highest)