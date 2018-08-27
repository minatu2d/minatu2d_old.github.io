import chainer
from chainer.backends import cuda
from chainer import Function, gradient_check, report, training, utils, Variable
from chainer import datasets, iterators, optimizers, serializers
from chainer import Link, Chain, ChainList
import chainer.functions as F
import chainer.links as L
from chainer.training import extensions
import numpy as np


class ExpAdd(Function):
    def forward_cpu(self, inputs):
        print("forward cpu")
        x, y = inputs
        z = np.exp(x) + np.exp(y)
        return z,

    def backward_cpu(self, inputs, grad_outputs):
        x, y = inputs
        gz, = grad_outputs

        gx = gz * np.exp(x)
        gy = gz * np.exp(y)
        return gx, gy

    def forward_gpu(self, inputs):
        cupy = cuda.cupy
        x, y = inputs
        z = cupy.exp(x) + cupy.exp(y)
        return z,

    def backward_gpu(self, inputs, grad_outputs):
        cupy = cuda.cupy
        x, y = inputs
        gz, = grad_outputs

        gx = gz * cupy.exp(x)
        gy = gz * cupy.exp(y)
        return gx, gy

def expadd(x, y):
    return ExpAdd().forward_cpu((x,y))

x = Variable(np.random.uniform(-1, 1, (3, 2)).astype(np.float32))
print("X :",x)
y = Variable(np.random.uniform(-1, 1, (3, 2)).astype(np.float32))
print("Y :",y)

w = expadd(x, y)
print("Type :",type(w))
print("Result :",w)
w.backward_cpu()
