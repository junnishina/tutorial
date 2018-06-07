# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 13:37:08 2017

@author: 022067
"""

from keras.applications.vgg16 import VGG16, preprocess_input, decode_predictions
from keras.preprocessing import image
import numpy as np
import sys

model = VGG16(include_top=True, weights='imagenet', input_tensor=None, input_shape=None)
img = image.load_img("4.2.04.tiff", target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)

preds = model.predict(preprocess_input(x))
results = decode_predictions(preds, top=5)[0]
for result in results:
    print(result)
