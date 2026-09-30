"""
Run a sentiment analysis of the sentence using Python
"""
import nltk 
from textblob import TextBlob 

text = 'The food was really good but the service was terrible.'
blob = TextBlob(text) 
for sentence in blob.sentences:
    print(sentence.sentiment)

# Output
Sentiment(polarity=0.05, subjectivity=0.6)