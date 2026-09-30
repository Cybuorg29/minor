def assign_values(list): 
    for i, val in enumerate(list): 
        if not val or val != val: 
            list[i] = 0
            
    return list

my_list = [5, 2, 3, None, '', 8] 
result = assign_values(my_list) 
print(result) 
# Output: [5, 2, 3, 0, 0, 8]