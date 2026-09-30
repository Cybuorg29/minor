"""
Create a program to check if a given string is a palindrome
"""

def is_palindrome(string):
    n = len(string)
    for i in range(n // 2):
        if string[i] != string[n-i-1]:
            return False
    return True

if __name__ == '__main__':
    print(is_palindrome("racecar"))