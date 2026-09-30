def count_items(lst, item):
    '''This function will return the total number of specific items in a list.'''
    return len([x for x in lst if x == item])