def get_middle_char(string):
    """Returns the middle character of a given string."""
    middle_index = int(len(string) / 2)
    return string[middle_index]

if __name__ == '__main__':
    string = "middle"
    print(get_middle_char(string))