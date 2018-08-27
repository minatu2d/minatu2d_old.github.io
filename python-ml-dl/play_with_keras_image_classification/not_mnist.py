#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 10:35:58 2018

@author: minatu2d
"""
from keras.preprocessing.image import ImageDataGenerator
import numpy as np

def load_data(dataset_dir="notMNIST_small", test_split=0.33):
    img_gen = ImageDataGenerator()
    not_mnist_generator = img_gen.flow_from_directory(dataset_dir, 
                                                      target_size = (28,28), 
                                                      class_mode='categorical'
                                                      )
    x_all = np.empty([])
    