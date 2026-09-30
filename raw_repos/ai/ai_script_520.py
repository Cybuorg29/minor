def convert_to_lowercase(list_of_strings):
    return [string.lower() for string in list_of_strings]

if __name__ == '__main__':
    string_list = ["UPPERCASE", "lOwErCaSe", "MiXeDcAsE"]
    print(convert_to_lowercase(string_list))