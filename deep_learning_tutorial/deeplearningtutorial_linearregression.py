# -*- coding: utf-8 -*-
"""DeepLearningTutorial_LinearRegression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NrvL0u-RqAemMsVWpK_hacGetDbPLK4t
"""

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

x_data = np.asarray([3.3,4.4,5.5,6.71,6.93,4.168,9.779,6.182,7.59,2.167,
                         7.042,10.791,5.313,7.997,5.654,9.27,3.1])
y_data = np.asarray([1.7,2.76,2.09,3.19,1.694,1.573,3.366,2.596,2.53,1.221,
                         2.827,3.465,1.65,2.904,2.42,2.94,1.3])
m = x_data.shape[0]

x_data = np.reshape(x_data,(m,1))
y_data = np.reshape(y_data,(m,1))

np.random.seed(2)
tf.set_random_seed(2)

plt.plot(x_data, y_data, 'ro', label='Data')

plt.legend()
x1,x2,y1,y2 = plt.axis()
plt.axis((2,12,-4,6))
plt.show()

display_step = 10
n_steps = 100    
n_iterations = []  
n_loss = []      
learned_weight = []  
learned_bias = []

learning_rate = 0.001

X = tf.placeholder(tf.float32, shape=(m, 1), name="input") 
y = tf.placeholder(tf.float32, shape=(m,1), name="label")

W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
b = tf.Variable(tf.zeros([1]))

y_hat = W * X + b

loss = (1/(2*m)) * tf.reduce_sum(tf.square(y_hat - y))

optimizer = tf.train.GradientDescentOptimizer(learning_rate)

train_step = optimizer.minimize(loss)

with tf.Session() as sess:
  
  sess.run(tf.global_variables_initializer())
  for step in range(n_steps):
    _, c = sess.run([train_step,loss], feed_dict={X: x_data, y: y_data})
    
    #Record Keeping
    n_iterations.append(step)
    n_loss.append(c)
    learned_weight.append(W.eval())
    learned_bias.append(b.eval())
  
    # Display logs per epoch step
    if (step+1) % display_step == 0:
            #c = sess.run(loss)
            print("Epoch:", '%04d' % (step+1), "Cost=", "{:.9f}".format(c), \
                "W=", sess.run(W), "b=", sess.run(b))
  


print("")

plt.plot(n_iterations,n_loss)
plt.ylabel('Loss')
plt.xlabel('Iterations')
plt.show()

plt.plot(x_data, y_data, 'ro', label='Data')
plt.plot(x_data, learned_weight[-1] * x_data + learned_bias[-1], label='Final Fitted Model')
plt.plot(x_data, learned_weight[0] * x_data + learned_bias[0], label='Initial Model')
plt.plot(x_data, learned_weight[25] * x_data + learned_bias[25], label='Iteration 25 Model')
plt.plot(x_data, learned_weight[50] * x_data + learned_bias[50], label='Iteration 50 Model')
plt.legend()
x1,x2,y1,y2 = plt.axis()
plt.axis((2,12,-4,4))
plt.show()

x_test = 3.0

y_prediction = learned_weight[-1] * x_test + learned_bias[-1]

print("x_test=3.0")
print("Prediction for x_test: " + str(y_prediction))

