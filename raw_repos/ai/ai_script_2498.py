def is_palindrome(num):
    num_str = str(num)
    # compare the first and last characters
    if num_str[0] != num_str[-1]:
        return False
    # go to the next pair of characters
    if len(num_str) >= 3:
        return is_palindrome(num_str[1:-1])
    # all characters have been compared, number is a palindrome
    return True