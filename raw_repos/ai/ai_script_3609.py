import tensorflow as tf 
#get the dataset
dataset = load_dataset()

# create the input pipeline
iterator = dataset.make_initializable_iterator()
next_element = iterator.get_next()

#build the model
model=Sequential()
#input layer
model.add(Conv2D(32,(3,3), activation='relu',input_shape=(input_width,input_height,input_channels)))
#max pooling
model.add(MaxPooling2D(pool_size=(2,2)))
#flatten
model.add(Flatten)
#hidden layer
model.add(Dense(64,activation='relu'))
#output layer
model.add(Dense(2,activation='sigmoid'))

#train model
model.compile(optimizer='SGD', Loss="binary_crossentropy",metrics=['accuracy'])
model.fit(dataset,epochs=5)