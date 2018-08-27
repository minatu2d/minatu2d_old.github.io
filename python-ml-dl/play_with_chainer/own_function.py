#
# https://docs.chainer.org/en/stable/guides/functions.html
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

class MulAdd(Function):
    def forward(self, inputs):
        x, y, z = inputs
        w = x * y + z
        return w,

    def backward(self, inputs, grad_outputs):
        x, y, z = inputs
        gw, = grad_outputs

        gx = y * gw
        gy = x * gw
        gz = gw
        return gx, gy, gz

x = Variable(np.random.uniform(-1, 1, (3, 2)).astype(np.float32))
print("x:",x)
y = Variable(np.random.uniform(-1, 1, (3, 2)).astype(np.float32))
print("y:",y)
z = Variable(np.random.uniform(-1, 1, (3, 2)).astype(np.float32))
print("z:",z)
print("MulAdd")
def muladd(x,y,z):
    return MulAdd()(x, y, z)

w = muladd(x,y,z) 
#print(w)
