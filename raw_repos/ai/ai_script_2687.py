def is_subset(s1, s2):
    for e in s1:
        if e not in s2:
            return False
    return True

is_subset({1,2,3}, {1,2,3,4,5,6}) # Output: True