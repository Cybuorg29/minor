"""
A code to implement Multiple Linear Regression for a given dataset
"""

import numpy as np

def multiple_linear_regression(X, y):
    '''
    This function accepts feature matrix X and target vector y,
    and returns the coefficients of the determined multiple linear regression model.
    '''
    X = np.concatenate((np.ones((X.shape[0], 1)), X), axis=1) 
    #concatenate a column of ones to X
    return np.linalg.inv(X.T @ X) @ X.T @ y