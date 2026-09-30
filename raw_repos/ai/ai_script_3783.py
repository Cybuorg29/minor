import pandas as pd 
  
data = {'Name':['Tom', 'nick', 'krish', 'jack'], 
        'Age':[20, 21, 19, 18] 
       } 

df = pd.DataFrame(data)  

cols = ['Name', 'Age']

# Creating new Dataframe  
df_new = df[cols] 

print(df_new)