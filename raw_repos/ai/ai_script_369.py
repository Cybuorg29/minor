import random

def generate_random_sequence(length):
    sequence = []
    for i in range(length):
        sequence.append(random.choice([0, 1]))
    return sequence