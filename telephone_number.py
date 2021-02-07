# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 11:42:35 2021
telephone_number.py
@author: kales
"""

# The Telephone class shows you how to check to see if a telephone number
# entered by the user is formatted as (xxx)xxx-xxxx upon entry.
# If properly formatted, we remove the () and - to format as xxxxxxxxxx
# If not properly formatted, we add the () and - back to format as (xxx)xxx-xxxx

# These constant fields hold the valid lengths of strings that are formatted
# and unformatted.
formatted_length = 13
unformatted_length = 10

valid = True # Flag to indicate valid format
telephone_number = input("Please enter the telephone number using this format (xxx)xxx-xxxx\n")

# Determine whether str is properly formatted
if (len(telephone_number) == formatted_length) and \
    telephone_number[0] == "(" and \
    telephone_number[4] == ")" and \
    telephone_number[8] == "-":
    valid = True
    print("Great! Telephone number", telephone_number, \
          "is a properly formatted telephone number.")
else:
    valid = False
    print("Yikes! Telephone number", telephone_number, \
          "is a not a properly formatted telephone number.")


# Accept telephone number as (xxx)xxx-xxxx and return as xxxxxxxxxx
# Strip the phone number and combine into a string
if valid == True:
    area_code = telephone_number[1:4:]
    three_digit_prefix = telephone_number[5:8:]
    line_number = telephone_number[9:13]
    unformatted_telephone_number = area_code + three_digit_prefix + line_number
    print("The telephone number input is now unformatted as", unformatted_telephone_number)

if valid == False:
    area_code = telephone_number[0:3]
    three_digit_prefix = telephone_number[3:6]
    line_number = telephone_number[6:10]
    formatted_telephone_number = "(" + area_code + ")" + three_digit_prefix + \
        "-" + line_number
    print("The unformatted telephone number input is now formatted as", \
          formatted_telephone_number)