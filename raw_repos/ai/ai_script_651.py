def print_score(score):
    try:
        score = int(score)
        print(f'The score is {score}')
    except ValueError:
        print("The score must be an integer.")