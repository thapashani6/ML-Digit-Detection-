# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 22:07:03 2019

@author: Shani
"""
import tensorflow as tf
CUDA_VISIBLE_DEVICES=0,1
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))