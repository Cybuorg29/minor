import random

def create_random_array():
    lst = []
    for i in range(4):
        lst.append(random.randint(1,10))

    return lst