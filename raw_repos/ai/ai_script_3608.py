# Imports
import nltk

# CKY Parsing
def cky_parse(sentence):
  """Given a sentence, apply CKY parsing to optimize the parsing of it"""
  
  words = nltk.word_tokenize(sentence)
  
  # Create tree structure
  table = [[None for i in range(len(words))] for j in range(len(words))]
  for j in range(len(words)):
    for i in reversed(range(j)):
      parts_of_speech = nltk.pos_tag(words[i:j+1])
      part_of_speech = tuple(tag for word,tag in parts_of_speech)
      if part_of_speech in grammar.productions():
        table[i][j] = part_of_speech
        break
  return table