def most_vowels(sentence):
    # Split sentence into words
    words = sentence.split(" ")
    # Keep track of our highest vowel count and the associated word
    highest_count = 0
    most_vowels_word = ""
    # Count the number of vowels in each word
    for word in words:
        num_vowels = 0
        for c in word:
            if c.lower() in ["a", "e", "i", "o", "u"]:
                num_vowels += 1
        # Store word if it has the highest vowel count
        if num_vowels > highest_count:
            highest_count = num_vowels
            most_vowels_word = word
    return most_vowels_word

if __name__ == "__main__":
    print(most_vowels("The quick brown fox jumps over the lazy dog.")) # prints brown