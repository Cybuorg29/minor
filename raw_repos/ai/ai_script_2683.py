def compare_strings(s1, s2):
    s1_chars = list(s1)
    s2_chars = list(s2)
    num_diff_chars = 0
    for char in s1_chars:
        if char not in s2_chars:
            num_diff_chars += 1
    for char in s2_chars:
        if char not in s1_chars:
            num_diff_chars += 1
    return num_diff_chars