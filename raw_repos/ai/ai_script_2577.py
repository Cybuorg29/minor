def unique_elements(input_list): 
    result_list = []
    for item in input_list: 
        if item not in result_list: 
            result_list.append(item)
    return result_list

input_list = [2, 3, 9, 5, 2, 4, 9]
print(unique_elements(input_list))
# Output: [2, 3, 9, 5, 4]