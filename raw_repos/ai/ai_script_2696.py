from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

# Vectorize the message into a format that the model can accept
vect = CountVectorizer().fit(X_train)
X_train_vectorized = vect.transform(X_train)

# Train a Logistic Regression model
model = LogisticRegression()
model.fit(X_train_vectorized, y_train)

# Use the model to predict the sentiment of a given message
message_sentiment = model.predict([vect.transform([message])])