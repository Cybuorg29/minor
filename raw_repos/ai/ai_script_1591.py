"""
Find the longest common substring between two strings
"""

def longest_common_substring(s1, s2):
    """Find the longest common substring between two strings.
    
    Args:
        s1 (str): The first string.
        s2 (str): The second string.
        
    Returns:
        str: The longest common substring.
    """
    max_length = 0
    longest_substring = ""
    len1, len2 = len(s1), len(s2)
    for i in range(len1): 
        for j in range(len2):
            length = 0
            while i + length < len1 and j + length < len2:
                if s1[i + length] != s2[j + length]:
                    break 
                length += 1
            if length > max_length:
                max_length = length
                longest_substring = s1[i : i + length]
    return longest_substring
    
if __name__ == '__main__':
    s1 = "Tangible"
    s2 = "Non-Tangible"
    print(longest_common_substring(s1, s2))