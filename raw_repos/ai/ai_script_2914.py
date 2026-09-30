"""
Given an array of English words, find any word which is an anagram of another word in the same array.
"""

def find_anagrams(words):
    anagrams = [] 
    for i in range(len(words)): 
        for j in range(i+1, len(words)): 
            if (sorted(words[i]) == sorted(words[j])): 
                anagrams.append((words[i],words[j])) 
    return anagrams

if __name__ == '__main__':
    words = ["listen", "pot", "part", "opt", "trap", "silent", "top"]
    print(find_anagrams(words))