def remove_duplicates(list_of_strings):
    """
    This function will take a list of strings and return a list of the same strings without duplicates.
    """
    unique_strings = list(set(list_of_strings))
    return unique_strings

list_of_strings = ["a", "b", "c", "a", "d"]
print(remove_duplicates(list_of_strings))