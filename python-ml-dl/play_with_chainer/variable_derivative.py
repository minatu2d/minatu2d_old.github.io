#
# https://docs.chainer.org/en/stable/guides/variables.html
#
import numpy as np
import chainer
from chainer.backends import cuda
from chainer import Function, gradient_check, report, training, utils, Variable
from chainer import datasets, iterators, optimizers, serializers
from chainer import Link, Chain, ChainList
import chainer.functions as F
import chainer.links as L
from chainer.training import extensions


x_data = np.array([5], dtype=np.float32)
print(x_data)

x = Variable(x_data)
print(x)

y = x**2 - 2 * x + 1
print(y)

print(y.array)
y.backward()
print(x.grad)

z = 2 * x
y = x ** 2 - 2 + 1
y.backward(retain_grad=True)
print(z.grad)

# Gradient of matrix
x = Variable(np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float32))
y = x**2 - 2*x + 1
y.grad = np.ones((2, 3), dtype=np.float32)
y.backward()
print(x.grad)

#
x = chainer.Variable(np.array([[0, 2, 3], [4, 5, 6]], dtype=np.float32))
y = x ** 3
y.grad = np.ones((2, 3), dtype=np.float32)
y.backward(enable_double_backprop=True)
print(x.grad_var)
