def get_nth_fibonacci_number(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return get_nth_fibonacci_number(n-1)+get_nth_fibonacci_number(n-2)