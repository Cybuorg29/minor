def get_frequency_map(string): 
    frequency_map = {}
    # count the frequency of each character
    for char in string: 
        if char in frequency_map:
            frequency_map[char] += 1
        else:
            frequency_map[char] = 1
    return frequency_map

string = "hello world"

frequency_map = get_frequency_map(string)
print(frequency_map)  # {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}