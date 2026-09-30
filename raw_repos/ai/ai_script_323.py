"""
Generate a best fit line for data points in Python
"""
import numpy as np

data = [(2,4), (4,7), (6,8), (7, 11)]

x = np.array([x[0] for x in data])
y = np.array([y[1] for y in data])

m, c = np.polyfit(x, y, 1)

print("Best-fit line equation: y = {:.2f}x + {:.2f}".format(m,c))