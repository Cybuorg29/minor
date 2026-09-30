def get_primes_in_range(a, b):
    primes = []
    for num in range(a, b + 1):
        if all(num % i != 0 for i in range(2, num)):
            primes.append(num)
    return primes