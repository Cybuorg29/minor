"""
Calculate the linear regression line for the given data
"""
import numpy as np

def linear_regression_line(X, Y):
    mean_x = np.mean(X)
    mean_y = np.mean(Y) 
    stdev_x = np.std(X)
    stdev_y = np.std(Y)

    numerator = 0
    for x, y in zip(X, Y):
        numerator += (x - mean_x) * (y - mean_y) 
    beta_1 = numerator/ (stdev_x * stdev_y)

    beta_0 = mean_y - (beta_1 * mean_x)
    
    return (beta_1, beta_0)

if __name__ == "__main__":
   X = [1, 2, 3, 4, 5]
   Y = [6, 8, 10, 11, 12]
   print("Linear Regression Line: {}".format(linear_regression_line(X, Y)))