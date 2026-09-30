def find_substring(string, substring):
    """
    Find the position of a substring in a string
    :param string: the string
    :param substring: the substring to find
    :return: the position of the substring in the string
    """
    for i in range(len(string) - len(substring) + 1):
        if string[i:i+len(substring)] == substring:
            return i
    return -1  # substring not found