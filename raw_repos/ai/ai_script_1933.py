import collections 
  
# function to get most frequently used word 
def most_frequent(string): 
  
    # split the string into list of words 
    split_it = string.split() 
      
    # pass the split_it list to instance of Counter class. 
    Counter = collections.Counter(split_it) 
  
    # most_common() produces k frequently encountered 
    # input values and their respective counts. 
    most_occur = Counter.most_common(1) 
  
    return most_occur[0][0]  
  
#Driver function 
text = "Machine learning is a subset of artificial intelligence and is a powerful tool in data science."
print(most_frequent(text))