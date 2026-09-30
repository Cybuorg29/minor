import nltk 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Preprocess data
training_data = [('I love this new phone!', 'positive'), ('This phone is terrible!', 'negative')]
all_words = []
documents = []
for (sent, category) in training_data:
    words = word_tokenize(sent)
    words = [word.lower() for word in words if word not in stopwords.words()]
    documents.append((words, category))
    all_words.extend(words)

# Create feature set
distinct_words = set(all_words)
feature_set = [({word: (word in tokenized_sentence) for word in distinct_words}, category) for (tokenized_sentence, category) in documents]

# Train model
classifier = nltk.NaiveBayesClassifier.train(feature_set)