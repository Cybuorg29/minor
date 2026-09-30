import pandas as pd
from sklearn.linear_model import LinearRegression

# load data
data = pd.read_csv('cars.csv')

# create feature matrix
X = data[['make', 'model']]

# set target variable
y = data['price']

# one-hot encode categorical make and model data
X = pd.get_dummies(X, columns=['make', 'model'])

# create and fit model
model = LinearRegression()
model.fit(X, y)