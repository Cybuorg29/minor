def sum_primes(n):
    # Initialize sum to 0
    sum_prime = 0

    # Iterate through all numbers from 0 to n
    for num in range(2, n+1):
        is_prime = True
        
        # Check whether the number is prime
        for div in range(2, num):
            if num % div == 0:
                is_prime = False
                break
        
        # If the number is prime, add it to the sum
        if is_prime:
            sum_prime += num

    # Return the sum
    return sum_prime