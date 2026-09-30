def median(numbers):
    sorted_numbers = sorted(numbers)

    if len(numbers) % 2 == 1:
        return sorted_numbers[len(numbers)//2]
    else:
        middle1 = sorted_numbers[len(numbers)//2]
        middle2 = sorted_numbers[len(numbers)//2 - 1]
        return (middle1 + middle2) / 2