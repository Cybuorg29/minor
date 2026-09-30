def second_largest(list_of_numbers):
    max_num = max(list_of_numbers)
    sec_max_num = None
    for num in list_of_numbers:
        if num != max_num and (sec_max_num is None or sec_max_num < num):
            sec_max_num = num
    return sec_max_num