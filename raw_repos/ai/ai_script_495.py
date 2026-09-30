import string
import random

def generate_password():
    # get all letters and digits
    chars = string.ascii_letters + string.digits + string.punctuation

    # generate a 8 character password from chars
    password = ''.join(random.sample(chars, 8))

    return password

# example
password = generate_password()
print(password) # >$z]e#43