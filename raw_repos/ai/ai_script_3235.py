def create_freq_table(lst): 
    freq_table = {} 
    for item in lst: 
        if (item in freq_table): 
            freq_table[item] += 1
        else: 
            freq_table[item] = 1
  
    return freq_table