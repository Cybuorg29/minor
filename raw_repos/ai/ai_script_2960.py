def analyze_string(input_string):
    '''This function analyzes a provided string of characters and 
    returns the number of occurrences of each character.'''
    dict_count = {}
    for char in input_string:
        if char in dict_count:
            dict_count[char] += 1
        else:
            dict_count[char] = 1
    return dict_count