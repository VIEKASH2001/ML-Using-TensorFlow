import tensorflow as tf

a=tf.constant(5)#this is called a constant node, this stores the constantvalue
b=tf.constant(6)
c=a*b

# Create the session object
sess = tf.Session()
 
#Run the graph within a session and store the output to a variable
output_c = sess.run(c)
 
#Print the output of node c
print(output_c)
 
#Close the session to free up some resources
sess.close()
