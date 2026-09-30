import keras

# Create a neural network
model = keras.Sequential([
    keras.layers.Dense(2, activation='sigmoid'),
    keras.layers.Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(X, y, epochs=1000)