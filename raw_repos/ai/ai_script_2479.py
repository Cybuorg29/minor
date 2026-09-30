def digit_sum(number):
    if number == 0:
        return 0
    return (number % 10) + digit_sum(number // 10)