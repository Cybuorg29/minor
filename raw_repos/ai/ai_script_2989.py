def num_common_characters(str1, str2):
    char_count = {}
    for c in str1:
        if c in str2:
            if c not in char_count:
                char_count[c] = 1
            else:
                char_count[c] += 1
    return sum(char_count.values())