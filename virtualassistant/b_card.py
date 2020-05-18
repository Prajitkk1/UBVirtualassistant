#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 14:08:55 2020

@author: Kavitha
"""
import re
import numpy as np
import sys
import cv2
#from business_card_parser import *
#from b_card import *
import sys


def email(data):
    email_address = ""
    e_char = '@'
    for line in data:
        split = line.split()
        for i in split:
            if e_char in i:
                email_address += i
            
    return email_address


def phone(data):
    bad_phone = ['pager', 'fax','pager:','pager-','fax:', 'fax-']
    phone_number = None
    phone_regex = "\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}"
    for line in data:
        match = re.search(phone_regex, line)
        if match:
            check = False
            split = line.split()
            for val in split:
                if val in bad_phone:
                    check = True
            if not check:
                phone_number = match.group() 
           
    return phone_number

def name(data):
    bad_name = ("Ventures", "Digital", "Works", "Inc", "Holdings", "Unlimited", "Dancer","Singer", "Labs", \
                         "Engineer", "Solutions", "Partners", "Technologies", "& son", "& co", "Brothers", "Tech",\
                         "Books", "Foods", "Industrial", "Innovation", "Bureau", "Prestige", "Direct", "Worldwide",\
                         "Online", "Properties", "Firm", "USA", "Development", "Technology", "Dynamics",\
                         "Consulting", "LTD", "Company", "Specialities", "Scientific", "Developer",\
                         "Brands", "Logistics", "Companies", "Creative", "Productions", "Graphics", "Prints",\
                         "University", "School","College")
    name= None    
    name_regex = "[\w\-.]{2,} [\w\-.]{2,}"
    for line in data:
#        print(line)
        match = re.search(name_regex, line)
        #print(match)
        if match:
            check = False
            split = line.split()
            for val in split:
                if val in bad_name:
                    check = True
            if not check:
                if name is None:
                    name = match.group() 
                
    return name
    

#fi = np.loadtxt('/Users/Kavitha/Desktop/CVIP/Project 3/myoutput.txt',delimiter='\t')
def card_details():
    temp =[]
    for line in (open('myoutput.txt', 'r').readlines()):
        line = line.strip()
        temp.append(line)
    name_ = name(temp)
    phone_number = phone(temp)
    email_id = email(temp)
    #print(name_, phone_number, email_id)
    f = (open('myoutput.txt', 'w'))
    f.truncate()
    #return None
    return name_, phone_number, email_id

#image_path = '/Users/Kavitha/Desktop/CVIP/Project 3/image_ocr.jpeg'
#k = card_details()
#print(k)

