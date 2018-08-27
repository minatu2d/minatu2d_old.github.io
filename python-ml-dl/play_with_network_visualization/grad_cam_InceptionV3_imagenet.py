#
#
# ORG :https://github.com/vense/keras-grad-cam
#
#

#
#
# GradCam : InceptionV3/ ImageNet Image
#
#

import keras
from keras.applications.inception_v3 import (
    InceptionV3, preprocess_input, decode_predictions)

from keras.preprocessing import image
from keras.layers.core import Lambda
from keras.models import Sequential
import keras.backend as K
import tensorflow as tf

import numpy as np
import sys
import cv2

PRE_TRAINED_NET="InceptionV3"

def load_image(img_path):
    '''
    Load and process input image
    '''
    print("Image must formatted as (N,W,H,C)")
    img = image.load_img(img_path, target_size=(299, 299))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    print(x.shape)
    return x

def normalize(x):
    # utility function to normalize a tensor by its L2 norm
    return x / (K.sqrt(K.mean(K.square(x))) + 1e-5)

def target_category_loss_output_shape(input_shape):
    return input_shape

def target_category_loss(x, category_index, nb_classes):
    return tf.multiply(x, K.one_hot([category_index], nb_classes))

def grad_cam(input_model, image, category_index,
        layer_name, n_class=1000, input_shape=(224,224)):
    '''
    Calculate gradient from the CNN layer
    '''
    nb_classes = n_class
    target_layer = lambda x: target_category_loss(x, category_index, nb_classes)

    x = input_model.layers[-1].output
    x = Lambda(target_layer, output_shape=target_category_loss_output_shape)(x)

    model = keras.models.Model(input_model.layers[0].input, x)

    loss = K.sum(model.layers[-1].output)
    conv_output = [l for l in model.layers if l.name == layer_name][0].output

    grads = normalize(K.gradients(loss, conv_output)[0])
    gradient_function = K.function([model.layers[0].input], [conv_output, grads])

    output, grads_val = gradient_function([image])
    output, grads_val = output[0, :], grads_val[0, :, :, :]

    weights = np.mean(grads_val, axis = (0, 1))
    cam = np.ones(output.shape[0 : 2], dtype = np.float32)

    for i, w in enumerate(weights):
        cam += w * output[:, :, i]

    cam = cv2.resize(cam, input_shape)
    cam = np.maximum(cam, 0)
    heatmap = cam / np.max(cam)

    #Return to BGR [0..255] from the preprocessed image (just for ImageNet)
    # (1, W, H, C) --> (W, H, C) format
    image = image[0, :]
    #image -= np.min(image)
    image += 1.
    #image = np.minimum(image, 255)
    image *= 127.5

    cam = cv2.applyColorMap(np.uint8(255 * heatmap), cv2.COLORMAP_JET)
    cam = np.float32(cam) + np.float32(image)
    cam = 255 * cam / np.max(cam)
    return np.uint8(cam), heatmap

def generate_gradcam_at_layer(model, layer_name, n_class = 1000, input_shape=(224,224)):
    '''
    Generating grad-cam and heatmap image at specified CNN layer
    '''
    predicted_class = np.argmax(predictions)
    cam, heatmap = grad_cam(model,
            preprocessed_input,
            predicted_class,
            layer_name,
            n_class=n_class,
            input_shape=input_shape,
            )
    gradcam_fn = "{0}_gradcam_{1}.jpg".format(PRE_TRAINED_NET, layer_name)
    heatmap_fn = "{0}_heatmap_{1}.jpg".format(PRE_TRAINED_NET, layer_name)
    cv2.imwrite(gradcam_fn, cam)
    cv2.imwrite(heatmap_fn, heatmap * 255)
    print("[",gradcam_fn, heatmap_fn,
            "] :was written as gradient at layer [{0}]".format(layer_name))
    return cam, heatmap

# Preprocessing input image as ImageNet
preprocessed_input = load_image(sys.argv[1])

# Load trained-model : InceptionV3 
print("Load {0} model, it takes a while...".format(PRE_TRAINED_NET))
model = InceptionV3(weights='imagenet')

# For summary
model.summary()

# Predict for input image
print("Predict class in 1000 class of ImageNet...")
predictions = model.predict(preprocessed_input)
top_1 = decode_predictions(predictions)[0][0]
print('Predicted class:')
print('%s (%s) with probability %.2f' % (top_1[1], top_1[0], top_1[2]))

# Generate Grad-Cam for the image
generate_gradcam_at_layer(model, "conv2d_94",
        n_class = 1000, input_shape = (299,299))

generate_gradcam_at_layer(model, "conv2d_93",
        n_class = 1000, input_shape = (299,299))

generate_gradcam_at_layer(model, "conv2d_92",
        n_class = 1000, input_shape =(299,299))
