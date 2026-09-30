def isPalindrome(string):
    '''This function will return whether or not a string is a palindrome.'''
    stack = [] 
    for letter in string:
        stack.append(letter)

    reverse = ''
    while stack:
        reverse += stack.pop()

    if reverse == string:
        return True
    return False