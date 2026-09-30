def highest_prime(num):
    highest_factor = 0
    for i in range(1, int(num**0.5)+1):
        if num % i == 0 and is_prime(i):
            highest_factor = i
    return highest_factor

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True