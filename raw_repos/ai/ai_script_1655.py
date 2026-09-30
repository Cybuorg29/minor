import random

def generate_random_set():
  generated_set = set()
  while len(generated_set) < 7:
    generated_set.add(random.randint(0, 10))
  return generated_set