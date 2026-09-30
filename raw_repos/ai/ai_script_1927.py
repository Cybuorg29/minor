from tensorflow.keras.layers import Input, LSTM, Dense

def seq2seq_model(src_length, trg_length, embedding_dim, num_enc_tokens, num_dec_tokens):
    # Define an input layer.
    encoder_inputs = Input(shape=(None, num_enc_tokens))
    # Add an LSTM layer with `src_length` number of units
    encoder_lstm = LSTM(src_length, return_state=True)
    # Define the encoder output, state and the encoder states
    encoder_outputs, state_h, state_c = encoder_lstm(encoder_inputs)
    # Discard `encoder_outputs` and only keep the states.
    encoder_states = [state_h, state_c]

    # Set up the decoder, using `encoder_states` as initial state.
    decoder_inputs = Input(shape=(None, num_dec_tokens))
    # Add an LSTM layer with `src_length` number of units
    decoder_lstm = LSTM(src_length, return_state=True, return_sequences=True)
    decoder_outputs, _, _ = decoder_lstm(decoder_inputs, initial_state=encoder_states)
    # Add a fully connected layer
    decoder_dense = Dense(trg_length, activation='softmax')
    # Define the output of the decoder
    decoder_outputs = decoder_dense(decoder_outputs)

    # Create a model
    model = Model([encoder_inputs, decoder_inputs], decoder_outputs)
    # Compile the model
    model.compile(optimizer='adam', loss='categorical_crossentropy')
    return model