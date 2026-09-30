def char_frequency(string): 
    counts = {}
    for char in string:
        if counts.get(char) == None: 
            counts[char] = 1
        else: 
            counts[char] += 1
    return counts