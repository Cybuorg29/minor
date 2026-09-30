def count_words(text):
    words = text.split()
    count = 0
    for word in words:
        count += 1
    return count

string = "Hello world"

# we need to add a check for empty string
if string != '':
    print(count_words(string))
else:
    print(0)