def print_elements(my_list):
    if not my_list: 
        return
    print(my_list[0])
    print_elements(my_list[1:])