def max_repeated_char(input_string):
    char_count = dict()
    max_count = 0
    max_char = None
    for char in input_string:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
            
    for char in char_count:
        if char_count[char] > max_count:
            max_count = char_count[char]
            max_char = char
    return max_char