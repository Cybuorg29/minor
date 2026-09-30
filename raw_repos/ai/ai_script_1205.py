def strip_string(s): 
    new_str = ""
    counts = {}
    
    # Create a dictionary to record the number of occurrences of each character
    for letter in s: 
        if letter not in counts:
            counts[letter] = 1
        else: 
            counts[letter] += 1
    
    for char in s: 
        if counts[char] > 1: 
            new_str += char
        counts[char] -= 1
    return new_str