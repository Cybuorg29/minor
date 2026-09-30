def is_prime_number(num):
    '''This algorithm will check if a given number is a prime number or not.'''
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

if __name__ == '__main__':
    num = 7
    print(is_prime_number(num))