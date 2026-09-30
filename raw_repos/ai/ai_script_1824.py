import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Read the dataset
data = pd.read_csv("data.csv")

# Split the data into features and labels
X = data.drop(['result'], axis=1)
y = data['result']

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, 
                                                    y, 
                                                    test_size=0.2, 
                                                    random_state=0)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)