from nltk.corpus import wordnet

# get the synset object 
synset = wordnet.synsets('cat')[0]

# find the hypernyms and count the number of hypernyms
count = len(list(synset.hypernyms()))

print("There are {} hypernyms of the word 'cat'.".format(count)) # prints There are 6 hypernyms of the word 'cat'.