from flask import Flask, request,jsonify
from flask import render_template,url_for,flash, redirect
from flask import send_from_directory
from virtualassistant import db
from virtualassistant import app as application
import os
from PIL import Image
from sqlalchemy import desc
import datetime
from virtualassistant.forms import RegistrationForm
from virtualassistant.models import User
import io
import cv2
import base64 
import numpy as np
import matplotlib.pyplot as plt
from virtualassistant import helpers


@application.route("/home",methods = ['POST', 'GET'])
@application.route("/",methods = ['POST', 'GET'])
def index():
    print(os.listdir())
    return render_template('index.html')


@application.route("/register",methods = ['POST', 'GET'])
def register():
    return render_template('register.html')


@application.route('/_image_recog' , methods = ['POST','GET'])
def image_recog():
    a = request.get_json().get('img_data')
    hello = helpers.stringToImage(a)
    print("yes it changed")
    #cv2.imwrite("hehe.png", hello)
    faces = helpers.find_image(hello)
    #print("no of faces"+ str(len(faces)))
    if len(faces)==1:
        name = helpers.detect_face_given_img(hello)
        flash(" your stupid face is detected")
        print("name" + str(name))
        return name
    elif len(faces)==2:
        flash(" not able to process two images at a time. One by One please")
        return "confused"
    return "received"


@application.route('/_ocr_recog' , methods = ['POST','GET'])
def ocr_recog():
    a = request.get_json().get('img_data')

    return "received"

@application.route('/_image_save' , methods = ['POST','GET'])
def image_save():
    a = request.get_json().get('img_data')
    hello = helpers.stringToImage(a)
    faces = helpers.find_image(hello)
    if len(faces)==1:
        helpers.save_new_images(hello, "new_name")
        return "success"
    elif(len(faces)==2):
        return "not success"
    return "not success"



@application.route('/unknown' , methods = ['POST','GET'])
def unknown():
    
    return render_template("unknown.html")



@application.route('/ocr' , methods = ['POST','GET'])
def ocr_screen():
    return render_template("ocr.html")


@application.route('/profile' , methods = ['POST','GET'])
def profile():
    name = request.args.get('name')
    return render_template("profile_page.html", name = name)

