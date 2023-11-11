# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 20:58:53 2022

@author: ACER
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import glob
from IPython.display import clear_output

def show_img(img):
    image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(image_rgb)
    plt.show()

def img_processing(img):
    #do something here
    return img

file_name = "./testdata/cat.jpg"
origin_img = cv2.imread(file_name)
show_img(origin_img)

result_img = img_processing(origin_img)
show_img(result_img)