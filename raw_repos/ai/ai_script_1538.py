def get_index_of_first_diff(string1, string2):
    # Get the length of the strings 
    len_1 = len(string1)
    len_2 = len(string2)

    # Get the length of the shorter string
    len_shorter = min(len_1, len_2)

    # Compare the two strings character by character
    for i in range(len_shorter):
        if string1[i] != string2[i]:
            # Return the index of the first differing character
            return i

# Get the index of first differing character
index = get_index_of_first_diff(string1, string2)

# Print the index
print(index)