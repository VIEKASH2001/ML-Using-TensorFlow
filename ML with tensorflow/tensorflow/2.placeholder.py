import tensorflow as tf

a = tf. placeholder(tf.float32)
b = tf. placeholder(tf.float32)
c = a*b

sess = tf.Session()
 
# Executing mul by passing the values [1, 3] [2, 4] for a and b respectively
output = sess.run(c, {a: [1,3], b: [2, 4]})
print('Multiplying a b:', output)


sess.close()
