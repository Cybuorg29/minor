def search(lst, item):
    for index, element in enumerate(lst):
        if element == item:
            return index
    return -1

search(lst, item)