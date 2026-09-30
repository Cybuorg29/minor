def longest_word_in_string(string):
    """
    A function to print out the longest word in a given string
    """
    words = string.split(" ")
    longest_word =  max(words, key=len)
    return longest_word

test_string = "This is an example sentence."

longest = longest_word_in_string(test_string)
print(longest) # example