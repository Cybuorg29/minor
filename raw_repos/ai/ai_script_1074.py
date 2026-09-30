"""
Write a code to generate a random 7 digit phone number.
"""

import random

def generate_random_phone_number():
    # create a list of digits
    lst = [str(i) for i in range(10)]
    
    # randomly select one digit
    random.shuffle(lst)
    
    # generate a 7-digit phone number
    phone_number = ''.join(lst[:7])
    
    return phone_number
    
if __name__ == '__main__':
    print(generate_random_phone_number()) # Output: e.g. 8247036