import random

def generate_random_array():
    array = []
    for i in range(10):
        array.append(random.randint(1,100))
    return array