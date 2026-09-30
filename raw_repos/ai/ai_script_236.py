import random

def game():
    options = ['rock', 'paper', 'scissors']

    player1 = random.choice(options)
    player2 = random.choice(options)

    if player1 == 'rock' and player2 == 'scissors':
        print("Player 1 Wins!")
    elif player1 == 'paper' and player2 == 'rock':
        print("Player 1 Wins!")
    elif player1 == 'scissors' and player2 == 'paper':
        print("Player 1 Wins!")
    elif player1 == 'scissors' and player2 == 'rock':
        print("Player 2 Wins!")
    elif player1 == 'rock' and player2 == 'paper':
        print("Player 2 Wins!")
    elif player1 == 'paper' and player2 == 'scissors':
        print("Player 2 Wins!")
    else:
        print("It's a draw!")