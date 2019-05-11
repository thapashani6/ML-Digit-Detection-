# -*- coding: utf-8 -*-
"""
Created on Fri May 10 04:22:23 2019

@author: Shani
"""

import numpy as np 
import matplotlib.pyplot as plt  
import glob 

image_list = []
for filename in glob.glob('*.jpeg'):
    im = Image.open(filename)
    image_list.append(im)  