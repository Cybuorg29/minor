def reverse_string(sentence):
    return ' '.join(sentence.split(' ')[::-1])

if __name__ == "__main__":
    sentence = "Where the wild things are"
    print(reverse_string(sentence))