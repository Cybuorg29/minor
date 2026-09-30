def remove_duplicates(numbers):
    new_list = []
    for num in numbers:
        if num not in new_list:
            new_list.append(num)
    return new_list