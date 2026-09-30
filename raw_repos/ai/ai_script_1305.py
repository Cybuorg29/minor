def print_pyramid(height):
    for row in range(1, height + 1):
        for col in range(1, row + 1):
            print('*', end=" ")
        print('\n')