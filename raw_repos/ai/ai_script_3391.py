def fibonacci(n):
    '''This function returns the n-th Fibonacci number.'''

    if n == 0 or n == 1:
        return n
    
    fib_n_1 = 0
    fib_n_2 = 1

    for i in range(2, n+1):
        fib_n = fib_n_1 + fib_n_2
        fib_n_1, fib_n_2 = fib_n_2, fib_n

    return fib_n