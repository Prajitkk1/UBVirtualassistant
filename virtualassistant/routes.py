from flask import Flask, request,jsonify
from flask import render_template,url_for,flash, redirect
from flask import send_from_directory
from virtualassistant import db
from virtualassistant.models import User
from virtualassistant import app as application
import os
import datetime
from virtualassistant.forms import RegistrationForm
from virtualassistant.models import User
import io
import cv2
import base64 
import numpy as np
import matplotlib.pyplot as plt
from virtualassistant import helpers
from virtualassistant.ocr_k import OCR_details,generate_string



@application.route("/home",methods = ['POST', 'GET'])
def index():
    #print(os.listdir())
    return render_template('index.html')

@application.route("/",methods = ['POST', 'GET'])
def start():
    return render_template('start.html')


@application.route("/register",methods = ['POST', 'GET'])
def register():
    name = request.args.get('name')
    email_id = request.args.get('email_id')
    ph_no = request.args.get('mobile_no')
    new_entry = User(name=name,email=email_id,mobile_no=ph_no)
    db.session.add(new_entry)
    db.session.commit()
    flash("you have been registered, please give some pose")
    helpers.train_new()
    return render_template('register.html',name = name,email_id = email_id, phone_no=ph_no)


@application.route('/_image_recog' , methods = ['POST','GET'])
def image_recog():
    a = request.get_json().get('img_data')
    hello = helpers.stringToImage(a)
    print("yes it changed")
    faces = helpers.find_image(hello)
    if len(faces)==1:
        name = helpers.detect_face_given_img(hello)
        if name=="error":
            return "confused"
        try_again = helpers.recheck_face(name, hello)
        if try_again==True:
            print("name" + str(name))
            return name
        else:
            print("try again return false")
            return "false"
    elif len(faces)==2:
        #flash(" not able to process two images at a time. One by One please")
        return "confused"
    return "received"


@application.route('/_ocr_recog' , methods = ['POST','GET'])
def ocr_recog():
    a = request.get_json().get('img_data')
    a = helpers.stringToImage(a)
    names = generate_string(a)
    names, ph_no, email = OCR_details(a)
    print("returning names" + str(names))
    print(names, ph_no,email)
    stt = "names=" + str(names) + "&&phone_no="+str(ph_no) + "&&email="+str(email)
    return stt


@application.route('/_image_save' , methods = ['POST','GET'])
def image_save():
    a = request.get_json().get('img_data')
    hello = helpers.stringToImage(a)
    faces = helpers.find_image(hello)
    name = request.get_json().get('name')
    print("name i founded"+ str(name))
    if len(faces)==1:
        helpers.save_new_images(hello, name)
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


@application.route('/ocr_details' , methods = ['POST','GET'])
def ocr_details():
    name = request.args.get('names')
    email_id = request.args.get('email')
    ph_no = request.args.get('phone_no')

    return render_template("ocr_checkdetails.html", name = name, email = email_id, mobile_no = ph_no)

@application.route('/profile' , methods = ['POST','GET'])
def profile():
    name = request.args.get('name')
    print(name)
    data1 = User.query.filter_by(name=str(name)).first()
    print(data1)
    email = data1.email
    mo = data1.mobile_no
    return render_template("profile_page.html", name = name,email = email,mob = mo)




@application.route('/_messages', methods = ['POST'])
def api_message():
    a = request.get_json().get('data')
    print(a)
    return "Binary message written!"


@application.route('/wrong_prediction', methods = ['GET','POST'])
def wrong_prediction():
    return render_template("wrong_predict.html")

@application.route('/contact', methods = ['GET','POST'])
def contact():
    return render_template("contact.html")

