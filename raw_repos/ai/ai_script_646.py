def longest_substring(str): 
    seen = {} 
    start = 0 
    maxlen = 0 
  
    for i, char in enumerate(str): 
        if char in seen: 
            start = max(start, seen[char] + 1) 
        seen[char] = i 
        maxlen = max(maxlen, i - start + 1) 
  
    return maxlen 
  
print(longest_substring("abcabcbb")) 
# Output: 3