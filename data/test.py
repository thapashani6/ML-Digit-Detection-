# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 19:12:37 2019

@author: Shani
"""
#!/usr/bin/python

#!/usr/bin/python
from PIL import Image
import os, sys

path = "D:/thapa/Documents/Rowan/eighth_Semester/ML/Yolo-digit-detector-master/data"
dirs = os.listdir( path )

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((200,200), Image.ANTIALIAS)
            imResize.save(f + ' resized.jpg', 'JPEG', quality=90)

resize()