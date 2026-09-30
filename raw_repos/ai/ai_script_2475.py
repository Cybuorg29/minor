def get_fibonacci_sequence(n):
    """Returns a list containing the Fibonacci sequence up to number n"""
    fib_list = [0, 1]
    if n <= 2:
        return fib_list[:n]
    
    for i in range(2, n):
        fib_list.append(fib_list[i-2] + fib_list[i-1])
    
    return fib_list

n = 10

fib_sequence = get_fibonacci_sequence(n)
print(fib_sequence) # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]