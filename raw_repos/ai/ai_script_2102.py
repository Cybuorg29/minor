def find_max(arr): 
    max_val = arr[0] 
    for i in range(len(arr)): 
        if max_val < arr[i]: 
            max_val = arr[i] 
    return max_val 

arr = [2, 4, 5, 7, 8] 
max_val = find_max(arr) 
print(max_val)