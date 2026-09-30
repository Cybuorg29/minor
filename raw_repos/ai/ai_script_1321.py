def print_table(dictionary):
    """Prints a table from a dictionary of lists."""
    # retrieve the lists
    names = dictionary['Name']
    ages = dictionary['Age']

    # print the table
    print('\tName\tAge')
    print('-' * 20)
    for i, name in enumerate(names):
        age = ages[i]
        print(f'\t{name}\t{age}')