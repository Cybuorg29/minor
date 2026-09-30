# Write an expression to check if a given number is a perfect square

import math

def is_perfect_square(num):
    return math.sqrt(num).is_integer()
    
# Check the given number
print(is_perfect_square(16)) # Output: True