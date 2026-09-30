def to_dictionary(arr):
    dict = {}
    for i in arr:
        dict[i[0]] = i[1]
    return dict

to_dictionary([('A',5), ('B', 3), ('C', 4), ('D', 7)])

# Output:
{'A': 5, 'B': 3, 'C': 4, 'D': 7}