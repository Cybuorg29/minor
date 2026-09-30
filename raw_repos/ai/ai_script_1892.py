def length_longest_substring(string):
    start = 0
    max_length = 0
    seen = {}
    for end in range(len(string)):
        # Check if the character has been previously seen.
        if string[end] in seen:
            # Move the starting point of the substring to the index after the last seen character of this character.
            start = max(start, seen[string[end]] + 1)
        # Update the index value of the last seen character.
        seen[string[end]] = end
        # Calculate the length of the current substring.
        max_length = max(max_length, end - start + 1)
    # Return the maximum length of the substring.
    return max_length