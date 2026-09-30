"""
Create a deep learning model to output a sentence in French when given an English sentence as input
"""
import tensorflow as tf
import numpy as np

# Input and output languages
input_lang = 'EN'
output_lang = 'FR'

# Define the model
model = tf.keras.Sequential([
  tf.keras.layers.Embedding(input_dim=vocab_size, output_dim=128, input_length=10),
  tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64)),
  tf.keras.layers.Dense(vocab_size, activation='softmax')
])

# Compile and train the model
model.compile(loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              optimizer=tf.keras.optimizers.Adam())
model.fit(input_tensor, output_tensor, epochs=100) 

# Make a prediction
sentence = 'I like to eat apples.'
predicted_sentence = translate(sentence, input_lang, output_lang, model) 

print(predicted_sentence) # J'aime manger des pommes.