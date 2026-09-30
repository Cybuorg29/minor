def select_list_items(list_of_strings, indexes, alphabet_string):
    new_list = []
    for index in indexes: 
        new_list.append(list_of_strings[alphabet_string.index(str(index))])
    return new_list

print(select_list_items(list_of_strings, indexes, alphabet_string)) # Output: ["Foo", "Baz"]