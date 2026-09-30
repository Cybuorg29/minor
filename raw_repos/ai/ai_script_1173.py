"""
Example of data visualization using Python's matplotlib library
"""  
import matplotlib.pyplot as plt

#Create two datasets
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

#Plot the data
plt.plot(x_values, y_values)

#Label the axes
plt.xlabel('x values')
plt.ylabel('y values')

#Show the plot
plt.show()