def get_frequency(input):
    # Split the input into words
    words = input.split()

    # Create a dictionary to store the words and the frequency
    frequency = dict()

    # Iterate over the words and store the frequency
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
            
    return frequency

if __name__ == "__main__":
    # Input string
    input = "the quick brown fox jumps over the lazy dog"

    # Get the frequency of words
    frequency = get_frequency(input)

    # Print the frequency
    print(frequency)