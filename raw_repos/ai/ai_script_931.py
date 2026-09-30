def find_max(list):
    # base condition
    if len(list) == 1:
        return list[0] 
    else:
        # compare the current element to the next element
        max_element = max(list[0], list[1])
        # remove the compared element
        list.pop(1)
        # call the function on the remaining list
        return find_max(list[:1] + [max_element] + list[1:])