import string
import random

def generate_random_string(length):
    allowed_characters = string.ascii_lowercase
    return ''.join(random.choices(allowed_characters, k=length))

random_string = generate_random_string(5)
print(random_string)