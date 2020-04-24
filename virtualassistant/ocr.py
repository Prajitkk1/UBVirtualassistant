#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 13:15:16 2020

@author: Kavitha
"""
import cv2
import numpy as np
import pytesseract
from PIL import Image

# Path of working folder on Disk

def get_string(img_path):
    # Read image with opencv
    img = cv2.imread(img_path)

    # Convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#    result = pytesseract.image_to_string(img)

#     Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img1 = cv2.dilate(img, kernel, iterations=1)
    img2 = cv2.erode(img1, kernel, iterations=1)

    # Write image after removed noise
    cv2.imwrite("removed_noise.png", img2)
    result = pytesseract.image_to_string(img2)


    return result
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    
k = get_string('hehe.png')
print(k)

print ("------ Done -------")
 