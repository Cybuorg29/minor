# prime number sieve
def prime_numbers(n): 
 
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
        if (prime[p] == True): 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
  
    prime_numbers = []
    for p in range(2, n): 
        if prime[p]: 
            prime_numbers.append(p)
    return prime_numbers[:10]
  
if __name__ == "__main__":
    n = 100
    print(prime_numbers(n))