def find_substring(str):
    substrings = []
    for length in range(1, len(str)+1):
        for start in range(len(str)- length + 1):
            substrings.append(str[start:start+length])
    return substrings