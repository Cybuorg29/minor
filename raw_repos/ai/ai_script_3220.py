def extract_name(string):
    """
    Parse a given string and extract the name from it.

    Parameters
    ----------
    string : str
        The string to parse

    Returns
    -------
    name : str
        The extracted name
    """
    # Split the string by words
    words = string.split()
    
    # The last word is the name
    name = words[-1]

    return name

string = "Hi! My name is John Smith"
print(extract_name(string)) # Outputs "John Smith"