def remove_once(arr): 
    freq_table  = {} 
    for num in arr: 
        if num in freq_table.keys(): 
            freq_table[num] += 1
        else: 
            freq_table[num] = 1

    filtered_array = [] 
    for num, freq in freq_table.items(): 
        if freq > 1: 
            filtered_array.append(num) 
    return filtered_array

remove_once([1, 2, 2, 3, 3, 3, 4, 4])

#Output: [2, 3, 4]