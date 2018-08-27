from keras.applications.inception_v3 import InceptionV3
from keras.applications import VGG16
from keras.preprocessing import image
from keras.models import Model
from keras.layers import Dense, GlobalAveragePooling2D
from keras import backend as K
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import ModelCheckpoint

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

img_width, img_height = 224, 224
PRE_TRAINED_NET="VGG16"
DATASET="MONKEY"

base_dir = '/home/tupv/work/data/10_monkey_species/'

train_data_dir = base_dir+ 'training'
validation_data_dir = base_dir + 'validation'
nb_train_samples = 1360
nb_validation_samples = 272
epochs = 50
batch_size = 16
n_class = 10

if K.image_data_format() == 'channels_first':
    input_shape = (3, img_width, img_height)
else:
    input_shape = (img_width, img_height, 3)

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
    class_mode='categorical')

validation_generator = test_datagen.flow_from_directory(
    validation_data_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='categorical')

# Create validation image generator


# create the base pre-trained model
#base_model = InceptionV3(weights='imagenet', include_top=False, input_shape=input_shape)
base_model = VGG16(weights='imagenet', include_top=False, input_shape=input_shape)

# add a global spatial average pooling layer
x = base_model.output
x = GlobalAveragePooling2D()(x)
# let's add a fully-connected layer
x = Dense(1024, activation='relu')(x)
# and a logistic layer -- let's say we have 200 classes
predictions = Dense(n_class, activation='softmax')(x)

# this is the model we will train
model = Model(inputs=base_model.input, outputs=predictions)

# first: train only the top layers (which were randomly initialized)
# i.e. freeze all convolutional InceptionV3 layers
for layer in base_model.layers:
    layer.trainable = False

# compile the model (should be done *after* setting layers to non-trainable)
model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
print("N layers :",len(model.layers))
model.summary()

# train the model on the new data for a few epochs
#model.fit_generator(...)
# fine-tune the model
history = model.fit_generator(
    train_generator,
    steps_per_epoch=nb_train_samples // batch_size,
    epochs=5,
    validation_data=validation_generator,
    validation_steps=nb_validation_samples // batch_size)

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
plt.savefig("{0}_{1}_finetune_fewlayers_accracy.png".format(PRE_TRAINED_NET, DATASET))
plt.show()
# summarize history for loss
plt.figure()
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.savefig("{0}_{1}_finetune_fewlayers_loss.png".format(PRE_TRAINED_NET, DATASET))
plt.show()

# at this point, the top layers are well trained and we can start fine-tuning
# convolutional layers from inception V3. We will freeze the bottom N layers
# and train the remaining top layers.

# let's visualize layer names and layer indices to see how many layers
# we should freeze:
for i, layer in enumerate(base_model.layers):
   print(i, layer.name)

# we chose to train the top 2 inception blocks, i.e. we will freeze
# the first 249 layers and unfreeze the rest:
for layer in model.layers[:17]:
    print(layer.name,"not trainable")
    layer.trainable = False
for layer in model.layers[17:]:
    print(layer.name,"trainable")
    layer.trainable = True

# we need to recompile the model for these modifications to take effect
# we use SGD with a low learning rate
from keras.optimizers import SGD
model.compile(optimizer=SGD(lr=0.0001, momentum=0.9), loss='categorical_crossentropy',
        metrics=['accuracy'])
model.summary()

# we train our model again (this time fine-tuning the top 2 inception blocks
# alongside the top Dense layers
best_val_acc_weight = '{0}_{1}_weight_best.hdf5'.format(PRE_TRAINED_NET, DATASET)
checkpoint = ModelCheckpoint(best_val_acc_weight, monitor='val_acc', verbose=1, save_best_only=True,
        mode='max')
history = model.fit_generator(
   train_generator,
   steps_per_epoch=nb_train_samples // batch_size,
   epochs=epochs,
   validation_data=validation_generator,
   validation_steps=nb_validation_samples // batch_size,
   callbacks=[checkpoint]
   )

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
plt.savefig("{0}_{1}_finetune_accracy.png".format(PRE_TRAINED_NET, DATASET))
plt.show()

# summarize history for loss
plt.figure()
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.savefig("{0}_{1}_finetune_loss.png".format(PRE_TRAINED_NET, DATASET))
plt.show()
