def lcm(a, b): 
    lcm = (a*b)//gcd(a,b) 
    return lcm

def gcd(a,b): 
    if a == 0 : 
        return b 
          
    return gcd(b%a, a)