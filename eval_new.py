# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 13:02:22 2019

@author: Shani
"""
#this evaluation file runs but gets really bad outputs with weights trainged by the default images
import json
import cv2
from yolo.backend.utils.box import draw_scaled_boxes
import os
import yolo
from yolo.frontend import create_yolo
import matplotlib.pyplot as plt

yolo_detector = create_yolo("ResNet50", ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"], 416)
DEFAULT_CONFIG_FILE = os.path.join(yolo.PROJECT_ROOT, "svhn", "config.json")
DEFAULT_WEIGHT_FILE = os.path.join(yolo.PROJECT_ROOT, "svhn", "weights.h5")
yolo_detector.load_weights(DEFAULT_WEIGHT_FILE)

DEFAULT_IMAGE_FOLDER = os.path.join(yolo.PROJECT_ROOT, "data")

img_files = [os.path.join(DEFAULT_IMAGE_FOLDER, "2298.jpeg"), os.path.join(DEFAULT_IMAGE_FOLDER, "2350.jpeg")]
imgs = []
for fname in img_files:
    img = cv2.imread(fname)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    imgs.append(img)
    plt.imshow(img)
    plt.show()

THRESHOLD = 0.3
for img in imgs:
    boxes, probs = yolo_detector.predict(img, THRESHOLD)

    # 4. save detection result
    image = draw_scaled_boxes(img,
                              boxes,
                              probs,
                              ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])

    print("{}-boxes are detected.".format(len(boxes)))
    plt.imshow(image)
    plt.show()