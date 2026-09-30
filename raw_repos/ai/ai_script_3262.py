def find_primes(n):
    primes=[]
    for num in range(2, n+1):
        for n in range(2, num):
            if num%n==0:
                break
            
        else:
            primes.append(num)
    return primes