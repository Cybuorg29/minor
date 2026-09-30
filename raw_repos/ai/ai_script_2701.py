"""
Determine whether a given string is a palindrome using stack data structure.
"""

def is_palindrome(string):
    # reverse the string
    stack = []
    for char in string:
        stack.append(char)

    rev_string = ""
    while stack:
        rev_string = rev_string + stack.pop()

    # compare reversed string with original string
    if rev_string == string:
        return True
    else:
        return False

if __name__ == '__main__':
    string = "racecar"
    print(is_palindrome(string))