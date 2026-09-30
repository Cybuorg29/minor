import numpy as np 
  
# Creating the 3D tensor 
X = np.zeros((10000, 32, 32)) 
  
# Initializing it with the grayscale images 
X[:,:,:] = dataset