# import libraries 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# read in the data 
data = pd.read_csv('email_data.csv')

# split into training and test data
X_train, X_test, y_train, y_test = train_test_split(data['text'], data['label'], test_size=0.33, random_state=42)

# create vectorizer and transform training data
count_vector = CountVectorizer()
count_train = count_vector.fit_transform(X_train)

# create and train a Naive Bayes model
NB_classifier = MultinomialNB()
NB_classifier.fit(count_train,y_train)

# transform test data
count_test = count_vector.transform(X_test)

# predict test labels
preds = NB_classifier.predict(count_test)