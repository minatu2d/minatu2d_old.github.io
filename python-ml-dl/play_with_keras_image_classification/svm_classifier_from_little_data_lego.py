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
import numpy as np
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dropout, Flatten, Dense
from keras import applications

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# dimensions of our images.
img_width, img_height = 150, 150

PRE_TRAINED_NET="VGG16_on_Lego"

top_model_weights_path = PRE_TRAINED_NET + 'bottleneck_fc_model.h5'

base_dir = '/home/tupv/work/data/lego_brick_images/images/'

train_data_dir = base_dir+ 'train'
validation_data_dir = base_dir + 'valid'
nb_train_samples = 6368
nb_validation_samples = 6368
epochs = 20
batch_size = 16


def save_bottlebeck_features():
    datagen = ImageDataGenerator(rescale=1. / 255)

    # build the VGG16 network
    model = applications.VGG16(include_top=False, weights='imagenet')

    generator = datagen.flow_from_directory(
        train_data_dir,
        target_size=(img_width, img_height),
        batch_size=batch_size,
        class_mode=None,
        shuffle=False)
    bottleneck_features_train = model.predict_generator(
        generator, nb_train_samples // batch_size)
    np.save(open(PRE_TRAINED_NET+'bottleneck_features_train.npy', 'wb'),
            bottleneck_features_train)
    np.save(open(PRE_TRAINED_NET+'bottleneck_features_train_label.npy', 'wb'),
            np.array(generator.classes[:bottleneck_features_train.shape[0]]))

    generator = datagen.flow_from_directory(
        validation_data_dir,
        target_size=(img_width, img_height),
        batch_size=batch_size,
        class_mode=None,
        shuffle=False)
    bottleneck_features_validation = model.predict_generator(
        generator, nb_validation_samples // batch_size)
    np.save(open(PRE_TRAINED_NET+'bottleneck_features_validation.npy', 'wb'),
            bottleneck_features_validation)
    np.save(open(PRE_TRAINED_NET+'bottleneck_features_validation_label.npy', 'wb'),
            np.array(generator.classes[:bottleneck_features_train.shape[0]]))


def train_top_model():
    train_data = np.load(open(PRE_TRAINED_NET + 'bottleneck_features_train.npy','rb'))
    train_labels = np.load(open(PRE_TRAINED_NET + 'bottleneck_features_train_label.npy','rb'))
#    train_labels = np.array(
#        [0] * (nb_train_samples // 2) + [1] * (nb_train_samples // 2))

    validation_data = np.load(open(PRE_TRAINED_NET + 'bottleneck_features_validation.npy','rb'))
    validation_labels = np.load(open(PRE_TRAINED_NET + 'bottleneck_features_validation_label.npy','rb'))
#    validation_labels = np.array(
#        [0] * (nb_validation_samples // 2) + [1] * (nb_validation_samples // 2))

    x_train = train_data.reshape(train_data.shape[0],-1)
    y_train = train_labels[:train_data.shape[0]]
    x_test = validation_data.reshape(validation_data.shape[0],-1)
    y_test = validation_labels[:validation_data.shape[0]]
    print("X train :",x_train.shape)
    print("Y train :",y_train.shape)
    print("X test :",x_test.shape)
    print("Y test :",y_test.shape)

    # Using SVM with multi-class
    from sklearn.svm import SVC
    from sklearn.multiclass import OneVsRestClassifier
    from sklearn.metrics import accuracy_score
    C = 1.
    kernel = 'rbf'
    gamma  = 0.01
    estimator = SVC(C=C, kernel=kernel, gamma=gamma)
    classifier = OneVsRestClassifier(estimator)
    classifier.fit(x_train, y_train)
    y_pred = classifier.predict(x_test)

    classifier2 = SVC(C=C, kernel=kernel, gamma=gamma)
    classifier2.fit(x_train, y_train)
    y2_pred = classifier2.predict(x_test)

    print('One-versus-the-rest: {:.5f}'.format(accuracy_score(y_test, y_pred)))
    print('One-versus-one :{.5f}'.format(accuracy_score(y_test, y2_pred)))

#    model = Sequential()
#    model.add(Flatten(input_shape=train_data.shape[1:]))
#    model.add(Dense(256, activation='relu'))
#    model.add(Dropout(0.5))
#    model.add(Dense(1, activation='sigmoid'))
#
#    model.compile(optimizer='rmsprop',
#                  loss='binary_crossentropy', metrics=['accuracy'])
#
#    history = model.fit(train_data, train_labels,
#              epochs=epochs,
#              batch_size=batch_size,
#              validation_data=(validation_data, validation_labels))
#    # Save models
#    model.save_weights(top_model_weights_path)
#    # list all data in history
#    print(history.history.keys())
#    # summarize history for accuracy
#    plt.plot(history.history['acc'])
#    plt.plot(history.history['val_acc'])
#    plt.title('model accuracy')
#    plt.ylabel('accuracy')
#    plt.xlabel('epoch')
#    plt.legend(['train', 'test'], loc='upper left')
#    plt.show()
#    plt.savefig("second_try_accuracy.png")
#    # summarize history for loss
#    plt.plot(history.history['loss'])
#    plt.plot(history.history['val_loss'])
#    plt.title('model loss')
#    plt.ylabel('loss')
#    plt.xlabel('epoch')
#    plt.legend(['train', 'test'], loc='upper left')
#    plt.show()
#    plt.savefig("second_try_loss.png")
#    #model.save_weights(top_model_weights_path)


#save_bottlebeck_features()
train_top_model()
