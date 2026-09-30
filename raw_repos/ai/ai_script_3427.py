def square_root(number):
    """This program takes a number and calculates its square root."""
    return number**0.5

num = int(input("Enter a number: "))
print("The square root of ", num, " is ", square_root(num))