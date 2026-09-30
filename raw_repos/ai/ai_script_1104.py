import random

def shuffle(arr):
    random.shuffle(arr)
    return arr

result = shuffle([1, 2, 3, 4, 5])
print(result)