
import math
import tensorflow as tf

x = math.floor(3.2)
print(x)

a = tf.constant([1.0, 2.0], name='a')
b = tf.constant([2.0, 3.0], name='b')

result = a + b

print(result)
