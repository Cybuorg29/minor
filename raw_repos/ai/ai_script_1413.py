import random

rand_string = ''
for i in range(10):
    rand_string += random.choice(['a', 'b', 'c', 'd'])
    
print(rand_string)