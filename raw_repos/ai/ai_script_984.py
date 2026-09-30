#import necessary models
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

#split data into train and test sets
x_train, x_test, y_train, y_test = train_test_split(bank_data, credit_risk, test_size = 0.3)

#create the machine learning model
lr_model = LogisticRegression()

#train the model
lr_model.fit(x_train, y_train)