def is_palindrome(str):
    """Checks if a given string is a palindrome.
    
    Parameters:
    str (str): string to be tested
    """
    str = str.lower()
    return str[::-1] == str

if __name__ == '__main__':
    string = "racecar"
    print(is_palindrome(string))