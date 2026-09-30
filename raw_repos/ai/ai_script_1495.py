def toUpperCase(words):
    upper_words=[]
    for word in words:
      upper_words.append(word.upper())
    return upper_words

if __name__ == "__main__":
    print(toUpperCase(['cat','dog','apple']))