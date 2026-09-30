def gcd(a,b): 
    if(b==0): 
        return a 
    else: 
        return gcd(b,a%b) 
a = 10
b = 15
gcd = gcd(a,b) 
print(gcd)