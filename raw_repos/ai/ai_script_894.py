def count_words_with_letter_a(arr):
    count = 0
    for s in arr:
        if 'a' in s:
            count += 1
    return count

if __name__ == '__main__':
    words = ['foo', 'bar', 'baz']
    count = count_words_with_letter_a(words)
    print(count)