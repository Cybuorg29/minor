def to_camel_case(string):
    '''This function converts a given string to the CamelCase format'''
    res = ""
    for word in string.split():
        res += word[0].upper() + word[1:]
    return res