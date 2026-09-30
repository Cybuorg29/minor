import string
import random

def generate_password():
    alpha_list = list(string.ascii_letters) + list(string.digits)
    return ''.join([random.choice(alpha_list) for _ in range(8)])

random_password = generate_password()
print(random_password)
// Output: 4U4K5U6L