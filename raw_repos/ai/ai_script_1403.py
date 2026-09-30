"""
Train a machine learning model to classify cats and dogs
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend as K

# Setting up Image Data Generator
train_data_dir = 'data/train'
validation_data_dir = 'data/validation'

img_width, img_height = 100, 100
train_datagen = ImageDataGenerator(
 rescale=1. / 255,
 shear_range=0.2,
 zoom_range=0.2,
 horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1. / 255)

train_generator = train_datagen.flow_from_directory(
 train_data_dir,
 target_size=(img_width, img_height),
 batch_size=32,
 class_mode='binary')

validation_generator = test_datagen.flow_from_directory(
 validation_data_dir,
 target_size=(img_width, img_height),
 batch_size=32,
 class_mode='binary')

# Setting up the model
model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=(img_width, img_height, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy',
 optimizer='rmsprop',
 metrics=['accuracy'])

# Training the model
model.fit_generator(
 train_generator,
 steps_per_epoch=2000,
 epochs=50,
 validation_data=validation_generator,
 validation_steps=800)