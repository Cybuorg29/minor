import scikit-learn as sklearn

# Load the data
X = dataset[['email_body', 'send_from', 'subject', 'num_links']]
y = dataset['is_spam']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0, stratify=y)

# Train the model
classifier = sklearn.linear_model.LogisticRegression()
classifier.fit(X_train, y_train)

# Test the model
y_predicted = classifier.predict(X_test)

# Check the accuracy
accuracy = sklearn.metrics.accuracy_score(y_test, y_predicted) 
print("Accuracy score: {:.2f}".format(accuracy)) # Output: Accuracy score: 0.95