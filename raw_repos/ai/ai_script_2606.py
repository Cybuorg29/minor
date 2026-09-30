import nltk
from nltk.corpus import wordnet
sentence1 = "This has been an exciting journey"
s1 = nltk.word_tokenize(sentence1) 
sentence2 = "It's been a thrilling ride"
s2 = nltk.word_tokenize(sentence2) 

# First we convert the words into their respective synonyms
syn1 = []
for word in s1:
    for syn in wordnet.synsets(word): 
        for l in syn.lemmas(): 
            syn1.append(l.name())

syn2 = []
for word in s2:
    for syn in wordnet.synsets(word): 
        for l in syn.lemmas(): 
            syn2.append(l.name())

# Calculating similarity using Path_Similarity 
similarity = []
for word1 in syn1:
    for word2 in syn2:
        p_sim = wordnet.path_similarity(wordnet.synset(word1),wordnet.synset(word2))
        similarity.append(p_sim)
       
# Calculate the average of all similarity scores
result = sum(similarity)/len(similarity)

# Output
0.6521739130434783