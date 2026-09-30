import random

def guessing_game():
    secret_number = random.randint(0, 10)
    guess = int(input("Guess a number between 0 and 10: "))
    while guess != secret_number:
        print("Incorrect! Try again.")
        guess = int(input("Guess a number between 0 and 10: ")) 
    print("Correct!")