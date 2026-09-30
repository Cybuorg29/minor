import string
import random

def generate_password():
    length = random.randint(12, 24)
    pwd = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(length))
    return pwd