#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 10:03:10 2018

@author: minatu2d
"""
from keras.datasets import mnist
from keras.datasets import cifar10
from keras.datasets import cifar100
from keras.datasets import fashion_mnist
import not_mnist


def load_mnist():
    """
    Load MNIST
    
    # Return (x_train, y_train), (x_test, y_test)
    
    # Ref : https://keras.io/datasets/#datasets
    
    """
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    return (x_train, y_train), (x_test, y_test)

def load_fashion_mnist():
    """
    Load Fashion-MNIST
    
    # Return (x_train, y_train), (x_test, y_test)
    
    # Ref : https://keras.io/datasets/#datasets
    
    """
    (x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
    return (x_train, y_train), (x_test, y_test)

def load_not_mnist(img_dir):
    """
    Load not MNIST
    
    # Return (x_train, y_train), (x_test, y_test)
    
    """
    (x_train, y_train), (x_test, y_test) = not_mnist.load_data()
    return (x_train, y_train), (x_test, y_test)

def load_cifar10():
    """
    Load CIFAR10
    
    # Return (x_train, y_train), (x_test, y_test)
    
    # Ref : https://keras.io/datasets/#datasets
    
    """
    (x_train, y_train), (x_test, y_test) = cifar10.load_data()
    return (x_train, y_train), (x_test, y_test)

def load_cifar100():
    """
    Load CIFAR100
    
    # Return (x_train, y_train), (x_test, y_test)
    
    # Ref : https://keras.io/datasets/#datasets
    
    """
    (x_train, y_train), (x_test, y_test) = cifar100.load_data(label_mode='fine')
    return (x_train, y_train), (x_test, y_test)

