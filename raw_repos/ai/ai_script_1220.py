"""
Calculate the value of pi using mathematical methods
"""

def calculate_pi():
    pi = 0  
    n = 1000
    for n in range(n):
        pi += ((-1)**n)/(2*n+1)
    pi = pi*4
    return round(pi, 6)

if __name__ == '__main__':
    print(calculate_pi())

# Output
# 3.141593