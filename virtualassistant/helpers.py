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
import speech_recognition as sr
from os import listdir
from os.path import isfile, join

clf = None


def stringToImage(base64_string):
    imgdata = base64.b64decode(base64_string)
    imgdata =  Image.open(io.BytesIO(imgdata))
    return cv2.cvtColor(np.array(imgdata), cv2.COLOR_BGR2RGB)

def find_image(img):
    face_locations = face_recognition.face_locations(img)
    #no = len(face_locations)
    return face_locations

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
    print(hmm)
    return hmm


def recheck_face(name1,name2):
    no_trues = []
    mypath = os.getcwd() + "\\Images\\"+ name1 
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    #print(onlyfiles)
    unknown_face_encoding = face_recognition.face_encodings(name2)[0]
    for i in range(0,7):
        picture_of_1 = face_recognition.load_image_file(os.getcwd() + "\\Images\\"+ name1 +"\\" + onlyfiles[i] )
        my_face_encoding = face_recognition.face_encodings(picture_of_1)[0]
        results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)
        if results[0] == True:
            no_trues.append(i)
    print(len(no_trues))
    if len(no_trues)>=3:
        return True
    else:
        return False
        
    