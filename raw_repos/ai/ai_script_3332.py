def count_letters(string):
    letter_count = {}
    for char in string:
        if char not in letter_count:
            letter_count[char] = 1
        else:
            letter_count[char] += 1;
    return letter_count

print(count_letters(string))