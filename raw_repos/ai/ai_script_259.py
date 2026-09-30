def compress_string(string):
    current_char = string[0]
    compressed_string = current_char
    count = 1

    for char in string[1:]:
        if char == current_char: 
            count += 1
        else: 
            compressed_string = compressed_string + str(count) + char
            current_char = char 
            count = 1
    compressed_string = compressed_string + str(count)
    return compressed_string

print(compress_string(string))

# Output: a2b1c5a3