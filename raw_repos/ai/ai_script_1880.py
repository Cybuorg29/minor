def prime_numbers():
    prime_nums = []
    for i in range(10, 50):
        is_prime = True
        for j in range(2, i):
            if i%j ==0:
                is_prime = False
                break
        if is_prime:
            prime_nums.append(i)
    return prime_nums