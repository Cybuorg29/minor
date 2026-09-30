def check_permutation(string1, string2):
    if len(string1) != len(string2):
        # The strings can't be permutations if they are different lengths
        return False
    
    # Convert the strings to lists
    list1 = list(string1)
    list2 = list(string2)
    
    # Sort the lists to make comparison easier
    list1.sort()
    list2.sort()
    
    # Compare the elements in the sorted lists
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    
    return True

# Example
print(check_permutation("cat", "act")) # Output: True