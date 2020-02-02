import tensorflow as tf

var = tf.Variable( [0.4], dtype = tf.float32 )#(value,datatype(this is not necessary))


#To initialize all the variables in a TensorFlow program, you must explicitly call a special operation
##init = tf.global_variables_initializer()
##sess.run(init)
