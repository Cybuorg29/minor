def find_index(string): 
    for i in range(len(string)):  
        if string[i] != ' ': 
            return i 
    return -1

string = "    Hello world!"
print(find_index(string))