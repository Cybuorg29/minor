import sklearn
from sklearn.linear_model import LinearRegression

# Create feature and label
X = [[3,6,0.4,4,300]]
y = [[BostonHousePrice]]

# Create and fit the linear regression model
reg = LinearRegression().fit(X, y)

# Predict the output
prediction = reg.predict([[3,6,0.4,4,300]])[0][0]