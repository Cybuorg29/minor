import numpy as np

# Create a data set
X = np.array([[0, 0, 0], [0, 1, 0], [1, 0, 0], [1, 1, 0], [0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
y = np.array([0, 0, 0, 0, 1, 1, 1, 1])

# Build a Naive Bayes classifier
naive_bayes = GaussianNB()

# Train the classifier using the training data
naive_bayes.fit(X, y)