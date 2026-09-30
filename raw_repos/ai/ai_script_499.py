import tensorflow as tf
 
#Create placeholders
X = tf.placeholder(tf.float32, [None, 784])
y = tf.placeholder(tf.float32, [None, 10])

#Create first layer
W1 = tf.Variable(tf.truncated_normal([784, 300], stddev=0.1))
b1 = tf.Variable(tf.zeros([300]))
A1 = tf.nn.relu(tf.add(tf.matmul(X, W1), b1))

#Create second layer
W2 = tf.Variable(tf.truncated_normal([300, 100], stddev=0.1))
b2 = tf.Variable(tf.zeros([100]))
A2 = tf.nn.relu(tf.add(tf.matmul(A1, W2), b2))

#Create third layer
W3 = tf.Variable(tf.truncated_normal([100, 10], stddev=0.1))
b3 = tf.Variable(tf.zeros([10]))
A3 = tf.nn.sigmoid(tf.add(tf.matmul(A2, W3), b3))

#Define cross-entropy loss
loss = tf.reduce_mean(-tf.reduce_sum(y*tf.log(A3), reduction_indices=[1]))

#Define the accuracy
correct_prediction = tf.equal(tf.argmax(A3,1), tf.argmax(y,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

#Train the model
train_op = tf.train.AdamOptimizer(1e-4).minimize(loss)