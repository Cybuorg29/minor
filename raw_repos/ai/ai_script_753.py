def compare_lists(my_list, pre_defined_list):
    new_list = []
    for element in my_list:
        if element in pre_defined_list:
            new_list.append(element)
    return new_list