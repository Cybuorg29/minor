def fibonacci_sequence(n):
    a, b = 0, 1
    fib_series = [a]
    while b < n:
        fib_series.append(b)
        a, b = b, a+b
    return fib_series

print(fibonacci_sequence(n)) #[0, 1, 1, 2, 3]