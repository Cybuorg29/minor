def filter_positives(numbers):
    result_list = []
    for element in numbers:
        if element >= 0:
            result_list.append(element)
    return result_list