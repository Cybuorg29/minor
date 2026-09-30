import tensorflow as tf
from tensorflow import keras 

# create a model
model = keras.Sequential()

# add a convolutional layer
model.add(keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(28, 28, 1)))

# add a max pooling layer
model.add(keras.layers.MaxPool2D((2,2)))

# add a flatten layer
model.add(keras.layers.Flatten())

# add a Dense layer
model.add(keras.layers.Dense(128, activation='relu'))

# add second Dense layer
model.add(keras.layers.Dense(10, activation='softmax'))

# compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])