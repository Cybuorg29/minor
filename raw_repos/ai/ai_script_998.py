import pandas as pd
import numpy as np

# Define features
features = ["wing_shape", "size", "tails_length", "color_pattern"] 

# Load the data
data = pd.read_csv("birds.csv")

# Preprocess the data to generate feature vectors
X = np.array(data[features]) 

# Make a target vector 
y = np.array(data["species"]) 

# Divide the data into training and test sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a classification model
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Generate evaluation metrics
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, y_pred)

print("Model accuracy: %.2f" % accuracy)