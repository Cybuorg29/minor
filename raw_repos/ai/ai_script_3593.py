def create_dictionary(keys, values):
    # Create an empty dictionary
    my_dict = {}
    # Populate the dictionary with elements from lists
    for i in range(len(keys)): 
        my_dict[keys[i]] = values[i]
    return my_dict