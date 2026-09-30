import tensorflow as tf

# Define the model.
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(10, activation="relu"),
    tf.keras.layers.Dense(1)
])

# Compile the model.
model.compile(optimizer="adam", loss="mse")

# Train the model.
model.fit([1, 2, 3], [8.5], epochs=50)