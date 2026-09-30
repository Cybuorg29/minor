def is_triangle_number(num):
    number = 0
    for i in range(num+1):
        number += i
        if number == num:
            return True
    return False