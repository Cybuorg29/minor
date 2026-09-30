import pandas as pd

data = [
 {'Name': 'Alice', 'Age': 25, 'City': 'London' },
 {'Name': 'Bob', 'Age': 32, 'City': 'Tokyo' }
 ]

data_frame = pd.DataFrame(data)
print(data_frame)

Output:
Name  Age     City
0  Alice    25    London
1    Bob    32     Tokyo