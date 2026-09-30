def sort_string_list(strings, alphabet):
    sorted_list = sorted(strings, key=lambda x:(alphabet.index(x[0]),x))
    return sorted_list