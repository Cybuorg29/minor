"""
Create a function that takes two numbers and returns their greatest common divisor in Python.
"""

def greatest_common_divisor(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return a
    if a > b:
        return greatest_common_divisor(a - b, b)
    return greatest_common_divisor(a, b - a)

if __name__ == '__main__':
    print(greatest_common_divisor(20, 25))  # 5