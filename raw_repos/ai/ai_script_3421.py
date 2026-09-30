import numpy as np 
import tensorflow as tf

# Create the model 
model = tf.keras.models.Sequential([
  tf.keras.layers.Dense(2, activation='sigmoid', input_shape=(3,))
]) 

# Compile the model 
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy']) 

# Create the input and output data 
input_data = np.array([[x1, x2, x3]])
output_data = np.array([[y1, y2]])

# Train the model 
model.fit(input_data, output_data, epochs=100)