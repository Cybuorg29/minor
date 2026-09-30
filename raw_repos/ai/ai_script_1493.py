def gcd(a, b, c): 
    if(b==0 and c==0): 
        return a 
    if(c==0): 
        return gcd(b, a % b) 
    return gcd(gcd(a, b), c)