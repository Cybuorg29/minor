import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

# run sentiment analysis
sentiment = analyzer.polarity_scores(text)

for key in sentiment:
    print('{0}: {1}'.format(key, sentiment[key]))

# output
compound: 0.6249
neg: 0.0
neu: 0.406
pos: 0.594