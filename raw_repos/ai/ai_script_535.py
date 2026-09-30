import string
import random

def generate_random_string(length):
    char_list = "".join(random.sample(string.ascii_letters, length))
    return char_list