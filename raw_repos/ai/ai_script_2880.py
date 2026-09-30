def check_zero(matrix):
    for row in matrix:
        for num in row:
            if num == 0:
                return True
    return False

print(check_zero(matrix))