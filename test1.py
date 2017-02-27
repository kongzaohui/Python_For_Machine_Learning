
'''
Created on 2017�~2��27��
@author: anton.kong
'''
import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))