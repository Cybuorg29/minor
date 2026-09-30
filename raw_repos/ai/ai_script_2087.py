"""
Write a script in Python that takes a list of strings and prints out the first letter of each string in uppercase
"""
# create the function
def uppercase_first_letters(list_of_strings):
    for string in list_of_strings:
        print(string[0].upper())

# call the function with the list
A = ["apple", "banana", "grapes"]
uppercase_first_letters(A)