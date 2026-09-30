import random

def generate_random_string():
  characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
  random_string = ''
  for x in range(5):
    random_string += random.choice(characters)
  
  return random_string

print(generate_random_string())