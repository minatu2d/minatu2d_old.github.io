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

from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from sklearn.model_selection import StratifiedKFold
from keras.callbacks import ModelCheckpoint
from keras.callbacks import TensorBoard 

import numpy as np
from keras import backend as K

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


# dimensions of our images.
img_width, img_height = 150, 150

base_dir = '/home/tupv/work/data/'

train_data_dir = base_dir+ 'train'
validation_data_dir = base_dir + 'validation'
nb_train_samples = 2000
nb_validation_samples = 800
epochs = 50
batch_size = 32

if K.image_data_format() == 'channels_first':
    input_shape = (3, img_width, img_height)
else:
    input_shape = (img_width, img_height, 3)

def create_model():
    model = Sequential()
    model.add(Conv2D(32, (3, 3), input_shape=input_shape))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(32, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(64, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Flatten())
    model.add(Dense(64))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(1))
    model.add(Activation('sigmoid'))

    model.compile(loss='binary_crossentropy',
                  optimizer='rmsprop',
                  metrics=['accuracy'])
    return model

# this is the augmentation configuration we will use for training
train_datagen = ImageDataGenerator(
    rescale=1. / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

# this is the augmentation configuration we will use for testing:
# only rescaling
test_datagen = ImageDataGenerator(rescale=1. / 255)

train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='binary')

validation_generator = test_datagen.flow_from_directory(
    validation_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='binary')

def get_data_from_generator(data_gen):
   x_list = np.array([]).reshape((0,) + data_gen.image_shape)
   y_list = np.array([])
   #x_list = []
   #y_list = []
   batch_index = 0
   while batch_index <= data_gen.batch_index:
       # Get one batch
       x_one_batch,y_one_batch = data_gen.next()
       # Add to list
       x_list = np.vstack([x_list, x_one_batch])
       y_list = np.append(y_list, y_one_batch)
       # Next batch
       batch_index = batch_index + 1

   X = np.asarray(x_list)
   y = np.asarray(y_list)
   return X, y

X_train = np.array([])
y_train = np.array([])
X_validation = np.array([])
y_validation = np.array([])

TRAIN_HD5_FILE="train_data.hf5"
X_train = np.load(open(TRAIN_HD5_FILE+"_X","rb"))
y_train = np.load(open(TRAIN_HD5_FILE+"_y","rb"))
if (X_train.shape[0] == 0):
    X_train, y_train = get_data_from_generator(train_generator)
    np.save(open(TRAIN_HD5_FILE+"_X", "wb"), X_train)
    np.save(open(TRAIN_HD5_FILE+"_y", "wb"), y_train)
else:
    print("Got TRAIN data in cache")

print(X_train.shape)
print(y_train.shape)

VALIDATION_HD5_FILE="validation_data.hf5"
X_validation = np.load(open(VALIDATION_HD5_FILE +"_X", "rb"))
y_validation = np.load(open(VALIDATION_HD5_FILE +"_y", "rb"))
if (X_validation.shape[0] == 0):
    X_validation, y_validation = get_data_from_generator(validation_generator)
    np.save(open(VALIDATION_HD5_FILE+"_X", "wb"), X_validation)
    np.save(open(VALIDATION_HD5_FILE+"_y", "wb"), y_validation)
else:
    print("Got VALIDATION data in cache")
print(X_validation.shape)
print(y_validation.shape)

#seed = 7
#kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=seed)
#cv_scores= []
#kfold_id = 0
#for cv_train, cv_test in kfold.split(X_train, y_train):
#    print(len(cv_train), len(cv_test))
#    print(cv_train[:10])
#    print(cv_test[:10])
#    # Create model
#    model = create_model()
#    # Fit model
#    #checkpointer = ModelCheckpoint(filepath='kfold_{0:02d}'.format(kfold_id) + '.hdf5', verbose=1, save_best_only=True)
#    tensor_board = TensorBoard(log_dir='./logs')
#    model.fit(X_train[cv_train], y_train[cv_train], epochs = epochs, batch_size = 32,
#            validation_data=(X_train[cv_test], y_train[cv_test]), callbacks = [tensor_board])
#    # Evaluate model
#    scores = model.evaluate(X_validation, y_validation, verbose=1)
#    print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
#    cv_scores.append(scores[1] * 100)
#    kfold_id = kfold_id + 1
#
#print("%.2f%% (+/- %.2f%%)" % (np.mean(cv_scores), np.std(cv_scores)))
model = create_model()
tensor_board = TensorBoard(log_dir='./logs')

history = model.fit(
    X_train, y_train,
    batch_size = batch_size,
    epochs=epochs,
    validation_data=(X_validation, y_validation),
    callbacks= [tensor_board]
    )

#history = model.fit_generator(
#    train_generator,
#    steps_per_epoch=nb_train_samples // batch_size,
#    epochs=epochs,
#    validation_data=validation_generator,
#    validation_steps=nb_validation_samples // batch_size)

model.save_weights('first_try.h5')

# list all data in history
print(history.history.keys())
# summarize history for accuracy
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
plt.savefig("first_try_accuracy.png")
# summarize history for loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
plt.savefig("first_try_loss.png")

