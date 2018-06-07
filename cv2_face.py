# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 10:55:17 2017

@author: 022067
"""

import cv2
print(cv2.__version__)
import os
os.getcwd()
face_cascade_path = './haarcascade_frontalface_default.xml'
#face_cascade_path = './lbpcascade_frontalface_improved.xml'
eye_cascade_path = './haarcascade_eye.xml'

face_cascade = cv2.CascadeClassifier(face_cascade_path)
eye_cascade = cv2.CascadeClassifier(eye_cascade_path)

img = cv2.imread('4.2.04.tiff')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

cv2.imwrite('lena_face_detect.jpg', img)

