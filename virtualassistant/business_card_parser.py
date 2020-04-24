#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 12:05:42 2020

@author: Kavitha
"""

import re


class Contact_info:

    def __init__(self, name, phoneNumber, emailAddress):
        self.name = name
        self.phoneNumber = phoneNumber
        self.emailAddress = emailAddress

    # Returns the full name of the individual (eg. Kavitha mohan, Prajit kr)
    def get_name(self):
        return self.name

    # Returns the phone number formatted as a sequence of digits with no punctuation
    def get_phone_num(self):
        return self.phoneNumber

    # Returns the email address of the individual
    def get_email_id(self):
        return self.emailAddress


class Business_card:

    name_disqualifiers = ("ENGINEER", "DEVELOPER", "LTD", "INC", "TECHNOLOGIES", "COMPANY", "DANCER", "Labs", \
                         "Ventures", "Solutions", "Partners", "Holdings", "& son", "& co", "Brothers", "Tech",\
                         "Books", "Foods", "Industrial", "Innovation", "Bureau", "Prestige", "Direct", "Worldwide",\
                         "Online", "Properties", "Firm", "USA", "Development", "Technology", "Dynamics",\
                         "Consulting", "Works", "Unlimited", "Specialities", "Scientific", "Digital",\
                         "Brands", "Logistics", "Companies", "Creative", "Productions", "Graphics", "Prints",\
                         "University", "School","College")
    
    phone_disqualifiers = ("FAX", "PAGER", "CELL")

    # Given the business card text, return the persons name contained, or None if not found
    @staticmethod
    def name(text):

        name_regex = "[\w\-.]{2,} [\w\-.]{2,}"

        for name in re.findall(name_regex, text):
            # Seperate the contents of this name by a space
            name_parts = name.upper().split(" ")

            #extract the name from potential outliers
            disqualify_name_parts = set(name_parts).intersection(Business_card.name_disqualifiers)
            if not disqualify_name_parts:
                return name

    # Given the business card text, return the phone number contained, or None if not found
    @staticmethod
    def phone_number(text):

        phone_regex = "(?:\+\d{1,3})?\s?\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{4}"

        # Iterate through each line of the document
        for line in text.splitlines():
            # Search the line for a substring matching the regex
            match = re.search(phone_regex, line)

            if match:
                if not any(s in line.upper() for s in Business_card.phone_disqualifiers):
                    
                    #extracting the phone number from potential outliers
                    extract_phone_num = re.sub("[^0-9]", "", match.group())
                    return extract_phone_num

    # Given the business card text, return the email address contained, or None if not found
    @staticmethod
    def email_address(text):
        email_regex = "[a-zA-Z0-9_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"

        # Find the email address in the document, if more than one match is found,
        # only the first is returned
        match = re.search(email_regex, text)
        if match:
            email_id = match.group()
            return email_id

    @staticmethod
    def get_info(text):
        
        return Contact_info(Business_card.name(text),
                            Business_card.phone_number(text),
                            Business_card.email_address(text))
        
     
 
