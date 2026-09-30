def sortByLength(sentence):
    words = sentence.split(' ')
    sortedWords = sorted(words, key=len)
    return sortedWords