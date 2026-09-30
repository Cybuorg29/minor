def get_common_elements(list1, list2):
    """
    Function to get all the common elements in two lists.
    
    Arguments:
        list1 {list}: The first list.
        list2 {list}: The second list.
    
    Returns:
        list: A list containing all the common elements in both lists.
    """
    common_elements = []
    for element in list1:
        if element in list2:
            common_elements.append(element)
    return common_elements