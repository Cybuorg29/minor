import re

text = "The conference will be held on Wednesday, June 16th, 2021"

# Extract dates
dates = re.findall(r'\d{1,2}[-/.]\d{1,2}[-/.]\d{2,4}',text) 

# Print the dates
for date in dates:
    print(date)
    
# Output
# 06/16/2021