def capitalize_string(string):
    words = string.split(' ')
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)

string = "this is a test string" 
capitalize_string(string)