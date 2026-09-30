def is_string_palindrome(str):
    reverse_str = str[::-1] 
    if reverse_str == str:
        return True
    else:
        return False