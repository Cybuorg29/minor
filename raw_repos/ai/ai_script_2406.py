def find_palindrome_pairs(words): 
    res = [] 
    for i in range(len(words)): 
  
        for j in range(len(words)): 
            if i != j: 
                word = words[i] + words[j] 
                if word == word[::-1]: 
                    res.append((i, j)) 
    return res 
print(find_palindrome_pairs(words))