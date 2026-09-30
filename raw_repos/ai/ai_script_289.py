from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Load data
iris_data = load_iris()
X = iris_data.data
y = iris_data.target

# Create a model and train it
model = RandomForestClassifier()
model.fit(X, y)

# Make predictions
predictions = model.predict(X)