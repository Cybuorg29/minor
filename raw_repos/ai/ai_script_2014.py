import keras
import numpy as np
from keras.layers import Dense
from keras.models import Sequential

# Building a Sequential model
model = Sequential()
# Input layer with 2 neurons
model.add(Dense(2, input_dim=64, activation='relu'))
# Hidden layer with 3 neurons
model.add(Dense(3, activation='relu'))
# Output layer with 15 neurons (15 classes)
model.add(Dense(15, activation='softmax'))

# Compiling and training the model
model.compile(loss='mean_squared_error',
              optimizer='adam',
              metrics=['accuracy'])
model.fit(training_samples, labels, epochs=100)