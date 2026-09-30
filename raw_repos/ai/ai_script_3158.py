def count_occurences(str, word):
    return str.count(word)

if __name__ == '__main__':
    str = 'Python is a great language. Python is easy to learn.'
    print(count_occurences(str, 'Python'))