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
from virtualassistant.business_card_parser import *
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def generate_string(image):

    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img1 = cv2.dilate(img, kernel, iterations=1)
    img2 = cv2.erode(img1, kernel, iterations=1)


    # Recognize text with tesseract for python
    string = pytesseract.image_to_string(img2)
    f = open('myoutput.txt', 'w')
    f.write(string)

    return string


    