def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

print("The GCD of {} and {} is {}".format(x, y, gcd(x, y)))