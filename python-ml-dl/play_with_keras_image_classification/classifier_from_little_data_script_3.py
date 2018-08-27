'''This script goes along the blog post
"Building powerful image classification models using very little data"
from blog.keras.io.
It uses data that can be downloaded at:
https://www.kaggle.com/c/dogs-vs-cats/data
In our setup, we:
- created a data/ folder
- created train/ and validation/ subfolders inside data/
- created cats/ and dogs/ subfolders inside train/ and validation/
- put the cat pictures index 0-999 in data/train/cats
- put the cat pictures index 1000-1400 in data/validation/cats
- put the dogs pictures index 12500-13499 in data/train/dogs
- put the dog pictures index 13500-13900 in data/validation/dogs
So that we have 1000 training examples for each class, and 400 validation examples for each class.
In summary, this is our directory structure:
```
data/
    train/
        dogs/
            dog001.jpg
            dog002.jpg
            ...
        cats/
            cat001.jpg
            cat002.jpg
            ...
    validation/
        dogs/
            dog001.jpg
            dog002.jpg
            ...
        cats/
            cat001.jpg
            cat002.jpg
            ...
```
'''

from keras import applications
from keras.preprocessing.image import ImageDataGenerator
from keras import optimizers
from keras.models import Sequential
from keras.layers import Dropout, Flatten, Dense
from keras import backend as K

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# path to the model weights files.
weights_path = 'vgg16_weights.h5'
top_model_weights_path = 'VGG16_bottleneck_fc_model.h5'
# dimensions of our images.
img_width, img_height = 150, 150

PRE_TRAINED_NET="VGG16_"

base_dir = '/home/tupv/work/data/'

train_data_dir = base_dir+ 'train'
validation_data_dir = base_dir + 'validation'
nb_train_samples = 2000
nb_validation_samples = 800
epochs = 2
batch_size = 32


if K.image_data_format() == 'channels_first':
    input_shape = (3, img_width, img_height)
else:
    input_shape = (img_width, img_height, 3)

# build the VGG16 network
model = applications.VGG16(weights='imagenet', include_top=False, input_shape=input_shape)
print("Number layer :",len(model.layers))
model.summary()
print(model.output_shape)
print('Model loaded.')

# build a classifier model to put on top of the convolutional model
top_model = Sequential()
top_model.add(Flatten(input_shape=model.output_shape[1:]))
top_model.add(Dense(256, activation='relu'))
top_model.add(Dropout(0.5))
top_model.add(Dense(1, activation='sigmoid'))
print("Number layer :",len(top_model.layers))
top_model.summary()

# note that it is necessary to start with a fully-trained
# classifier, including the top classifier,
# in order to successfully do fine-tuning
top_model.load_weights(top_model_weights_path)

# Combine VGG parts and fc layers into 1 Model
new_model = Sequential()
for layer in model.layers:
    new_model.add(layer)

# add the model on top of the convolutional base
# model.add(top_model)
new_model.add(top_model)
print("Number layer :",len(new_model.layers))
new_model.summary()

# set the first 25 layers (up to the last conv block)
# to non-trainable (weights will not be updated)
for layer in new_model.layers[:15]:
    print(layer.name,": not trainable")
    layer.trainable = False

# compile the model with a SGD/momentum optimizer
# and a very slow learning rate.
new_model.compile(loss='binary_crossentropy',
              optimizer=optimizers.SGD(lr=1e-3, momentum=0.9),
              metrics=['accuracy'])

# prepare data augmentation configuration
train_datagen = ImageDataGenerator(
    rescale=1. / 255,
    #shear_range=0.2,
    #zoom_range=0.2,
    #horizontal_flip=True
    )

test_datagen = ImageDataGenerator(rescale=1. / 255)

train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='binary')

validation_generator = test_datagen.flow_from_directory(
    validation_data_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='binary')

# fine-tune the model
history = new_model.fit_generator(
    train_generator,
    samples_per_epoch=nb_train_samples,
    epochs=epochs,
    validation_data=validation_generator,
    nb_val_samples=nb_validation_samples)


# Grad-CAM
from keras.preprocessing import image
import sys
import cv2
import numpy as np
from keras.preprocessing.image import load_img, img_to_array
import grad_cam


preprocessed_input = grad_cam.load_image(sys.argv[1], (150, 150))
#preprocessed_input = load_image("./examples/boat.jpg")
predictions = new_model.predict(preprocessed_input)
predicted_class = np.argmax(predictions)
#top_1 = VGG16.decode_predictions(predictions)[0][0]
print('Predicted class:',predicted_class)
#print('(%s) with probability ' % (["cat","dog"][predicted_class[0]]))

cam, heatmap = grad_cam.grad_cam(new_model,preprocessed_input, 
        predicted_class, "block5_conv3", (150,150))
cv2.imwrite("gradcam.jpg", cam)

# list all data in history
print(history.history.keys())
# summarize history for accuracy
plt.figure()
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.savefig("third_try_accuracy.png")
plt.show()
# summarize history for loss
plt.figure()
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.savefig("third_try_loss.png")
plt.show()
