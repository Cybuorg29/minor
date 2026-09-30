def has_palindrome(seq):
    """Returns True if the given sequence has a palindrome, otherwise returns False"""
    for num in seq:
        if str(num) == str(num)[::-1]:
            return True
    return False

if __name__ == '__main__':
    seq = [2332, 24124, 1221, 89898]
    print(has_palindrome(seq))