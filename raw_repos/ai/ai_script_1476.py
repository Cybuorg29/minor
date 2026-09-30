import matplotlib.pyplot as plt 
  
# Creating the data 
data = [2, 3, 5, 7, 9]  
  
# Creating the figure and axis 
fig, ax = plt.subplots()  
  
# plotting the barplot 
ax.bar(range(len(data)), data)  
  
# show the plot 
plt.show()