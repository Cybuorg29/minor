import numpy as np
from sklearn.linear_model import LinearRegression 

# Data
X_train = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y_train = np.array([6, 12, 18, 24, 30])

# Model 
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction
side_length = 3 
pred = model.predict([[side_length]])
print('The surface area for a cube with side length %.2f is %.2f' % (side_length, pred[0]))