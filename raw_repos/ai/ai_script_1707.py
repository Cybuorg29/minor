def compare_lists(list1, list2):
    length1 = len(list1) 
    length2 = len(list2) 
    common_values = list(set(list1).intersection(list2)) 
    return length1, length2, common_values