def reverse_string(str):
    if len(str) == 0: 
        return str 
    else:
        return reverse_string(str[1:]) + str[0]