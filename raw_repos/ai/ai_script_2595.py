import random

def generate_addition_equation():

    a = random.randrange(0, 6)
    b = random.randrange(0, 6)

    equation = str(a) + " + " + str(b) + " = "

    return equation