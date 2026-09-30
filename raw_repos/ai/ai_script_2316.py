def delete_element(given_list, element):
    for i in range(len(given_list)):
        if given_list[i] == element:
            del given_list[i]
            break
    return given_list