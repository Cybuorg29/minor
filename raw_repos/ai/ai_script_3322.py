import random
import string

def generate_password(length):
    char_types = list(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation)
    password = []
    for _ in range(length):
        ch = random.choice(char_types)
        while ch in password:
            ch = random.choice(char_types)
        password.append(ch)
 
    return ''.join(password)

password = generate_password(10)
print(password) # e.W8.vHc2e