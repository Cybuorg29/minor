import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Read data and split into training and test sets
data = pd.read_csv("customer_data.csv")
X = data.drop("target", axis=1)
y = data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Train the model
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Evaluate the model
score = clf.score(X_test, y_test)
print("Model accuracy:", score)