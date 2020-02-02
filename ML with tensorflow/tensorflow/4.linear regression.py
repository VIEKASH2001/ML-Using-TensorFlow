import tensorflow as tf

#y=b+W*x
# Creating variable for parameter slope or weight (W) with initial value as 0.4
W = tf.Variable([.4], tf.float32)
 
#Creating variable for parameter bias (b) with initial value as -0.4
b = tf.Variable([-0.4], tf.float32)
 
# Creating placeholders for providing input or independent variable, denoted by x
x = tf.placeholder(tf.float32)
 
# Equation of Linear Regression
linear_model = W * x + b
 
# Initializing all the variables
sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)
 
# Running regression model to calculate the CALCULATED Y
print(sess.run(linear_model,{x:[1, 2, 3, 4]}))

#y is the target value in here
y = tf.placeholder(tf.float32)#target value

#calculates SSE
error = linear_model - y
squared_errors = tf.square(error)
loss = tf.reduce_sum(squared_errors)

print(sess.run(loss, {x:[1,2,3,4], y:[2, 4, 6, 8]}))

#Creating an instance of gradient descent optimizer
optimizer = tf.train.GradientDescentOptimizer(0.01)#0.01 is the learning rate

#minimizes the loss by modifying W and b
train = optimizer.minimize(loss)

#in each iteration the optimizer is called and W,b values are modified
for i in range(1000):
     
     sess.run(train, {x:[1, 2, 3, 4], y:[2, 4, 6, 8]})
#the final weight and bias is displayed
print(sess.run([W, b]))
print(W)
