import tensorflow as tf

x = tf.constant([[1,2],[3,4]], dtype=tf.int32) 
y = tf.constant([[5,6],[7,8]], dtype=tf.int32)

#Sum operation
z = tf.add(x, y)

#Run in session
with tf.Session() as session:
  print(session.run(z))

# Output: 
# [[ 6  8]
#  [10 12]]