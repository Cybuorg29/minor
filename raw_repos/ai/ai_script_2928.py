import tensorflow as tf 

# Create a model
model = tf.keras.models.Sequential([
    # Add a convolutional layer with a 3x3 window
    tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(28, 28, 1)),
    # Add a Max Pooling layer
    tf.keras.layers.MaxPooling2D((2, 2)),
    # Add a Flatten layer
    tf.keras.layers.Flatten(),
    # Add a Dense layer with 10 neurons and a softmax activation function 
    tf.keras.layers.Dense(10, activation='softmax')
])
# Compile the model
model.compile(optimizer='adam',
   loss='sparse_categorical_crossentropy',
   metrics=['accuracy'])