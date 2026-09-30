def common_elements(list1, list2):
    list3 = []
    for i in list1:
        for j in list2:
            if i == j:
                list3.append(i)
    return list3