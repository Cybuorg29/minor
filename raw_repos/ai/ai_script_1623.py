def is_anagram(a, b):
    a = a.lower()
    b = b.lower()

    if len(a) != len(b):
        return False
    
    for char in a:
        if char not in b:
            return False
        b = b.replace(char, '', 1)
    
    return True

print(is_anagram("silent", "listen")) # Output: True