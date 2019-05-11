# -*- coding: utf-8 -*-
"""
Created on Fri May 10 03:44:30 2019

@author: Shani
"""

import os, sys
from PIL import Image

# open an image file (.bmp,.jpg,.png,.gif) you have in the working folder
imageFile = '3599.jpeg'
im1 = Image.open(imageFile)
# adjust width and height to your needs
width = 50
height = 50
# use one of these filter options to resize the image
im2 = im1.resize((width, height), Image.NEAREST)      # use nearest neighbour
  # best down-sizing filter
im2.save(imageFile)

