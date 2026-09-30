def non_repeating_characters(string):
    character_set = set() 
    for c in string: 
        if c not in character_set: 
            character_set.add(c)
    return list(character_set)

output = non_repeating_characters(string)
# Output: ['h', 'd', 'g', 'u', 'e', 'm', 'o', 'p', 'q', 't', 'v', 'i', 'c', 'b', 'k', 'x', 'f', 'z', 'a', 'y', 'r', 'w', 'l', 'n', 's', 'j']