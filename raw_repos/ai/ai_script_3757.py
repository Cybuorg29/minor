import pandas as pd 

data = {'Name': ['Jerry', 'Peter', 'Paul', 'John'], 
'Age': [20, 22, -18, 24]} 

df = pd.DataFrame(data)

df = df[df['Age'] >= 0]