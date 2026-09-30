"""
Please write a program that prints out the Fibonacci sequence from 1 to n.
"""
def fibonacci(n):
    fib = [1, 1]
    for i in range(2, n):
        a = fib[i-2]
        b = fib[i-1]
        fib.append(a+b)
    return fib[:n]

print(fibonacci(n)) # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]