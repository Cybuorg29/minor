"""
Print the first ten Fibonacci numbers
"""

def print_first_ten_fibonacci_numbers():
    """Print the first ten Fibonacci numbers."""

    n1, n2 = 0, 1
    num = 0
    while num < 10:
        print(n1)
        nth= n1 + n2
        n1 = n2
        n2 = nth
        num += 1
        
if __name__ == '__main__':
    print_first_ten_fibonacci_numbers()