"""
Generate a random DNA sequence of length 50
"""

import random

def random_dna_sequence(length):
    bases = ["A","T","G","C"]
    sequence = "".join([random.choice(bases) for _ in range(length)])
    return sequence

if __name__ == '__main__':
  print(random_dna_sequence(50))