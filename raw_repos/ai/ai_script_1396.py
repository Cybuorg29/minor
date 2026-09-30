def search_list(list_a, element):
    for i in range(len(list_a)):
        if list_a[i]==element:
            return i
    return -1