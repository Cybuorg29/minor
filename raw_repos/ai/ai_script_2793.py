import random 

def get_random_number():
    num = random.randint(-10, 10)
    if num < 0:
        num = -num
    return num