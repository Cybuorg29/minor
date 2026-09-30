import random

key = ''.join(random.choices(string.ascii_letters, k = 3))
value = random.randint(0, 9)
data = {key : value}