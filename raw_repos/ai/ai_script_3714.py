list1 = [9, 4, 8]
list2 = [1, 8, 5]
def add_corresponding_elements(list1, list2):
    result = []
    for i in range(len(list1)):
        result.append(list1[i] + list2[i])
    return result

print(add_corresponding_elements(list1, list2)) # Output: [10, 12, 13]