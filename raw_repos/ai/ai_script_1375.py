def find_longest_substring(string):
    """
    Finds the longest substring of unique characters in a given string.
    """
    longest_substring = ''
    current_substring = ''
    for ch in string:
        if ch not in current_substring:
            current_substring += ch
            if len(current_substring) > len(longest_substring):
                longest_substring = current_substring
        else:
            current_substring = ch
    return longest_substring