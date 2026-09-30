def find_first_non_repeating(string):
    seen = {}
    for char in string:
        if char in seen:
            seen[char] +=1 
        else:
            seen[char] = 1
    return [char for char in string if seen[char] == 1][0]