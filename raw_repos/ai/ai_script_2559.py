import random

random_string = ''.join(random.choices(['a', 'b', 'c'], k=10))
print(random_string)  # prints something like ccaacccaac