import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# 创建 w 和 b 节点，并设置初始值
w = tf.Variable([2.], dtype=tf.float32)
b = tf.Variable([1.], dtype=tf.float32)

x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)
# 创建线型模型
linear_model = w*x + b
# 创建损失模型
loss = tf.reduce_sum(tf.square(linear_model - y))

sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)
# print(sess.run(linear_model, {x:[1, 2, 3, 6, 8]}))
# print(sess.run(loss, {x:[1, 2, 3, 6, 8], y:[4.8, 8.5, 10.4, 21.0, 25.3]}))

# 创建一个梯度下降优化器
optimizer = tf.train.GradientDescentOptimizer(0.001)
train = optimizer.minimize(loss)

x_train = [1, 2, 3 ,6 ,8]
y_train = [4.8, 8.5, 10.5, 21.0, 25.3]

#### 训练10000 次
for i in range(10000):
    sess.run(train, {x:x_train, y:y_train})

print('w: %s b: %s loss: %s' % (sess.run(w), sess.run(
    b), sess.run(loss, {x: x_train, y: y_train})))