def is_anagram(string1, string2):
    # Make sure strings are the same length
    if len(string1) != len(string2):
        return False

    # Create dictionary of letter frequency for each string 
    char_freq1 = {}
    char_freq2 = {}

    # Iterate through each character in the strings
    for char in string1:
        char_freq1[char] = char_freq1.get(char, 0) + 1
    for char in string2:
        char_freq2[char] = char_freq2.get(char, 0) + 1

    # Compare the two dictionaries
    if char_freq1 == char_freq2:
        return True
    else:
        return False

if __name__ == '__main__':
    string1 = "elbon"
    string2 = "noble"
    print(is_anagram(string1, string2))