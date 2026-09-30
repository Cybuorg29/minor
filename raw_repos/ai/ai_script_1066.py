import nltk 
from nltk.sentiment.vader import SentimentIntensityAnalyzer 
sid = SentimentIntensityAnalyzer() 
ss = sid.polarity_scores(text) 

# Output
{'neg': 0.0, 'neu': 0.49, 'pos': 0.51, 'compound': 0.7717}