def count_substring(string, sub_string): 
    count = 0
  
    #Loop over the length of string 
    for i in range(0, len(string)): 
        # If a part of string matches with sub_string 
        #increment count  
        if (string[i:i+ len(sub_string)] ==sub_string): 
            count += 1
  
    return count 

count = count_substring(text, 'ab') 
print("Number of substring occurrences: ", count)