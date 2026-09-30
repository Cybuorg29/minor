"""
Function to format a number with two decimal places
"""

def two_decimals(num):
    """
    Format a number with two decimal places
    """
    return "{:.2f}".format(num)

if __name__ == '__main__':
    print(two_decimals(23.14159)) # prints 23.14