def find_common_letters(s1, s2):
    letters = set()

    for letter in s1:
        if letter in s2:
            letters.add(letter)
    return letters

# Example
s1 = 'apple'
s2 = 'oranges'
print(find_common_letters(s1, s2))
# Output: {'a', 'e'}