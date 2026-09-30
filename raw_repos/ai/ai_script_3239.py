# Create a frequency table for the given sequence
# using Python
from collections import Counter

string = 'aabbccddee'
# create the Counter object
freq_table = Counter(string)
# print the output
print(freq_table)

# Output
Counter({'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2})