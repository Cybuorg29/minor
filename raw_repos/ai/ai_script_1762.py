def count_letters(text):
    letter_count = {}
    for character in text:
        if character not in letter_count:
            letter_count[character] = 1
        else:
            letter_count[character] += 1
    return letter_count

print(count_letters(text))