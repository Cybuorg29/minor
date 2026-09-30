def fibonacci(n):
    fib_sequence = [1, 1]

    for i in range(2, n):
        new_num = fib_sequence[i-2] + fib_sequence[i-1]
        fib_sequence.append(new_num)

    return fib_sequence

fibonacci(10) # Output: [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]