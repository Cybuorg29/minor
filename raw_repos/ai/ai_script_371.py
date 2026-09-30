def detect_negative_number(numbers):
    flag = False
    for num in numbers:
        if num < 0:
            flag = True
            break
    return flag