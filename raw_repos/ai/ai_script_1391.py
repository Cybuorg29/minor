import random

rows = 5
columns = 6

matrix = [[random.randint(1,50) for c in range(columns)]for r in range(rows)]

for row in matrix:
    print(row)