def filter_length(strings):
    new_list = []
    for string in strings:
        if len(string) >= 2:
            new_list.append(string)
    return new_list

my_list = ["Hello","Hi","How","Are","You"]

print(filter_length(my_list))