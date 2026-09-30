import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# load dataset
dataframe = pd.read_csv('text_classification_data.csv')

# convert to vectors
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(dataframe['text'])

# split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(vectors, dataframe['label'], test_size = 0.25)

# create model
model = LogisticRegression()

# train model
model.fit(X_train,y_train)

# test model
predictions = model.predict(X_test)