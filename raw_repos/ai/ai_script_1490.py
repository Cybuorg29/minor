import random

# Generate 25 random numbers
random_list = []
for i in range(25):
    random_list.append(random.randint(0, 8))

print(random_list)