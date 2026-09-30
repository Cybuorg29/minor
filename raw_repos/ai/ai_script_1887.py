import random

def generate_random_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        matrix.append([])
        for j in range(cols):
            matrix[i].append(random.randint(0, 9))
    return matrix

if __name__ == '__main__':
    rows = 4
    cols = 4
    print(generate_random_matrix(rows, cols))