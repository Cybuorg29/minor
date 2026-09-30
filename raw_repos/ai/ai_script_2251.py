def split_string(string, character):
    return string.split(character)
    
if __name__ == '__main__':
    string = "A/B/C/D"
    character = "/"
    print(split_string(string, character)) # outputs ['A', 'B', 'C', 'D']