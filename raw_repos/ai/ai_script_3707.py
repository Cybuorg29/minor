def reverse_integer(x):
    rev_int = 0
    while x > 0:
        rev_int = rev_int * 10 + (x % 10)
        x //= 10
    return rev_int