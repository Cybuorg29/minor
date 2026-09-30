def compact_list(lst):
    # Define a new list to hold the compacted elements
    new_list = []
    current = None
    
    # Iterate through lst
    for item in lst:
        if item != current:
            current = item
            new_list.append(current)
    # Return the new list
    return new_list
    
# Call the function with the given list
my_list = [1,1,2,3,3,3,4,4,4,4,5]
print(compact_list(my_list)) # [1,2,3,4,5]