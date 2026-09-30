def prime_numbers():
    primes=[]
    for i in range (1,51):
        count=0
        for j in range (2,i):
            if i%j==0:
                count+=1
        if count==0:
            primes.append(i)
    return primes