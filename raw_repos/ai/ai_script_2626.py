def frequency_distribution(string):
    
    # create a dictionary of frequencies    
    freq_dict = {}
    for i in string:
        if i in freq_dict:
            freq_dict[i] += 1
        else:
            freq_dict[i] = 1
    
    # print the result
    for key, value in freq_dict.items():
        print (key + ': ' + str(value))