def my_function(my_list):
    output = []
    for i in range(0, len(my_list), 2):
        output.append(my_list[i] * 2)
    return output
By looping over the list in steps of two, the function will only have to go through half of the elements, thus optimizing the runtime.