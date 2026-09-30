"""
Generate the Fibonacci sequence of length 10 and print the result
"""

def get_fibonacci_sequence(length):
    a, b = 0, 1
    # generate the Fibonacci sequence
    sequence = []
    for _ in range(length):
        sequence.append(a)
        a, b = b, a + b
    # return the Fibonacci sequence
    return sequence

# get the Fibonacci sequence of length 10
fib_sequence = get_fibonacci_sequence(10)
# print the Fibonacci sequence
print(fib_sequence)