"""
Create a program to classify whether the given number is even or odd
"""

def even_or_odd(number: int) -> str:
    if number % 2 == 0:
        return 'even'
    else:
        return 'odd'

if __name__ == '__main__':
    print(even_or_odd(5))