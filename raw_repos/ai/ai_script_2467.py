def count_number(arr, number):
    count = 0
    for num in arr:
        if num == number:
            count += 1
    return count