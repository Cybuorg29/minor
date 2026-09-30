def convert_list_keys(list_of_data):
    key_dict = {}
    for item in list_of_data:
        key_dict[item[0]] = item
    return key_dict