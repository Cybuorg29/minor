"""
Create a text classifier using a Random Forest algorithm
"""
 
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# create the dataframe from the given input
df = pd.DataFrame(columns=['text', 'category'], data=input)

# define the features and labels
X = df['text']
y = df['category']

# create and train the model
model = RandomForestClassifier(n_estimators=100, random_state=0)
model = model.fit(X, y)