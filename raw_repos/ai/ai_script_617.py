import keras 

model = keras.Sequential()
model.add(keras.layers.Dense(256, activation="relu", input_dim=20))
model.add(keras.layers.Dense(128, activation="sigmoid"))
model.add(keras.layers.Dense(64, activation="softmax"))
model.add(keras.layers.Dense(1, activation="linear"))