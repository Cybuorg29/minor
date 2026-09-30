def repeat_last_two_char(string):
    """Takes a string as an argument and returns a new string with the last two characters repeated."""
    if len(string) < 2:
        return ""
    return string[:-2] + string[-2:] * 2