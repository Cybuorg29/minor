# import libraries 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# load the data
imdb = pd.read_csv('imdb.csv')

# Create feature vectors for training
vectorizer = CountVectorizer() 
X = vectorizer.fit_transform(imdb.TEXT)
y = imdb.SENTIMENT

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)
 
# Train a logistic regression classifier
lr = LogisticRegression(solver='lbfgs').fit(X_train, y_train)

# Evaluate the model performance
accuracy = lr.score(X_test, y_test)
print('Accuracy of sentiment classification model:', accuracy)