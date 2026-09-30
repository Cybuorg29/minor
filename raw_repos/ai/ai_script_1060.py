def compare_strings(string1, string2):
    """
    This function will compare two strings and return a boolean 
    depending on their equality or inequality. 
    """
    is_same = string1 == string2
    return is_same

string1 = 'hello' 
string2 = 'world'

print(compare_strings(string1, string2))