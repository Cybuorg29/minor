import random

def generate_random_string(length):
    """Generate a random string with given length using a set of lowercase and uppercase letters, numbers, and punctuation characters."""
    chars = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()[]{}\\|;:'"",./<>?"
    result = ""
    for i in range(length):
        result += random.choice(chars)
    return result

random_string = generate_random_string(10)
print(random_string) #eg. 7O?1Y%%&_K