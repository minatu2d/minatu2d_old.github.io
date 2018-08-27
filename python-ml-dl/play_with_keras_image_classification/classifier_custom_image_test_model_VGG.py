from keras.models import load_model
from keras.preprocessing.image import load_img, img_to_array
import sys
import numpy as np

weight_file =  sys.argv[1]
img_file = sys.argv[2]
print("Weight file :{0}".format(weight_file))

# returns a compiled model
# identical to the previous one
model = load_model(weight_file)
#for layer in model.layers:
#    print(layer.name)
model.summary()

# Load image
img = load_img(img_file, target_size=(224, 224))    # 画像ファイルの読み込み
img_array = img_to_array(img) / 255                                     #
img_list = []
img_list.append(img_array)
pre_proc_img = np.array(img_list)
pred = model.predict(pre_proc_img)
print(pred)

from keras.preprocessing import image
import sys
import cv2
import numpy as np
from keras.preprocessing.image import load_img, img_to_array
import grad_cam
from keras.applications.vgg16 import preprocess_input

#x = img_to_array(img)
#x = np.expand_dims(x, axis=0)
#x = preprocess_input(x)

predicted_class = np.argmax(pred)
print('Predicted class:',["cat", "dog"][predicted_class])

#cam, heatmap = grad_cam.grad_cam(model,pre_proc_img,
#        predicted_class, "conv2d_94", (150,150))
#cv2.imwrite("InceptionV3_gradcam_conv2d_94.jpg", cam)
#
#cam, heatmap = grad_cam.grad_cam(model,pre_proc_img,
#        predicted_class, "conv2d_93", (150,150))
#cv2.imwrite("InceptionV3_gradcam_conv2d_93.jpg", cam)
#
#cam, heatmap = grad_cam.grad_cam(model,pre_proc_img,
#        predicted_class, "conv2d_92", (150,150))
#cv2.imwrite("InceptionV3_gradcam_conv2d_92.jpg", cam)
#
#cam, heatmap = grad_cam.grad_cam(model,pre_proc_img,
#        predicted_class, "conv2d_10", (150,150))
#cv2.imwrite("InceptionV3_gradcam_conv2d_10.jpg", cam)
#
#cam, heatmap = grad_cam.grad_cam(model,pre_proc_img,
#        predicted_class, "conv2d_2", (150,150))
#cv2.imwrite("InceptionV3_gradcam_conv2d_2.jpg", cam)
#
#cam, heatmap = grad_cam.grad_cam(model,pre_proc_img,
#        predicted_class, "conv2d_3", (150,150))
#cv2.imwrite("InceptionV3_gradcam_conv2d_3.jpg", cam)


for layer in model.layers:
    if ("conv" in layer.name):
        name = layer.name
        cam, heatmap = grad_cam.grad_cam(model,pre_proc_img,
                predicted_class,name, (224,224))
        cv2.imwrite("VGG16_gradcam_{0}.jpg".format(name), cam)
        cv2.imwrite("VGG16_heatmap_{0}.jpg".format(name), heatmap * 255)
