def input_validation(input):
    try:
        input = int(input)
        if input >= 2 and input <= 6:
            return True
        else:
            return False
    except ValueError:
        return False