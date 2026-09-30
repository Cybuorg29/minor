def char_exists_in_string(s1, s2):
    for char in s2:
        if char not in s1:
            return False
    
    return True

if __name__ == '__main__':
    s1 = "hello world"
    s2 = "llo"
    print(char_exists_in_string(s1, s2))