"""
Construct a function to set up a dictionary with words and corresponding counts of occurrences of each word
"""
def word_count(string):
    word_dict = {}
    for word in string.split():
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    return word_dict

if __name__ == '__main__':
    print(word_count('hey hey hello hello hell oh hello'))