"""
Given an array containing words and a string, find the shortest word in the array that is a substring of the string.
"""

def find_shortest_substring(words, string): 
    min_length = float("inf")
    min_word = None
    for word in words:
        j = string.find(word)
        if j>-1 and len(word)<min_length:
            min_length = len(word)
            min_word = word
    return min_word

if __name__ == '__main__': 
    words = ["apple", "banana", "cat", "dog"]
    string = "aquickbrownfoxjumpsoverthelazydog"
    print(find_shortest_substring(words, string))