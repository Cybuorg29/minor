"""
def is_palindrome(num):
    # Initializing variables
    n = num
    rev = 0
    while (n > 0):
        # Storing the remainder
        rev = (rev * 10) + n % 10

        # Updating n
        n //= 10

    # Checking if the reversed number is equal to the given number
    if (num == rev):
        return True

    return False

# Function call
print(is_palindrome(1234321))
"""

Output: True