def remove_duplicates(arr): 
    result = [] 
    for item in arr: 
        if item not in result: 
            result.append(item) 
    return result

print(remove_duplicates(arr)) 
# Output: [1, 2, 3]