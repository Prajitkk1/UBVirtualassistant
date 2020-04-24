import io
import cv2
import base64 
import numpy as np
from PIL import Image
import face_recognition
from sklearn import svm
import os
from virtualassistant import face_detect
global clf
import random
import pytesseract

clf = None

def stringToImage(base64_string):
    imgdata = base64.b64decode(base64_string)
    imgdata =  Image.open(io.BytesIO(imgdata))
    return cv2.cvtColor(np.array(imgdata), cv2.COLOR_BGR2RGB)

def find_image(img):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    print("face detected" + str(len(faces)))
    return faces

def detect_face_given_img(img):
    global clf
    if clf is None:
        clf = face_detect.train_images()
    face_locations = face_recognition.face_locations(img)
    no = len(face_locations)
    if no>1:
        return "error"
    else:
        
        test_image_enc = face_recognition.face_encodings(img)[0]
        name = clf.predict([test_image_enc])
        print(*name)
        return name[0]
        
def train_new():
    clf = face_detect.train_images()
    
def save_new_images(img,name):
    rand_no = random.randrange(0,100)
    parent_dir = os.getcwd()+ "\\Images\\"
    directory = name
    path = os.path.join(parent_dir, directory)
    try:  
        os.mkdir(path)
    except:
        pass
    hmm = cv2.imwrite((path + '\\' + str(rand_no) +".png"), img)
    return hmm

        
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
def get_string(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((1, 1), np.uint8)
    img1 = cv2.dilate(img, kernel, iterations=1)
    img2 = cv2.erode(img1, kernel, iterations=1)
    result = pytesseract.image_to_string(img2)
    print("below is the string result")
    print(result)
    return result

    
        
        
        
        
        
        
        
        