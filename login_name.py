# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 11:54:20 2021
login_name.py
@author: kales
"""

import random

# get the user's first, middle, and last name and assign random number
first = input("Please enter your first name: ")
middle = input("Please enter your middle name: ")
last = input("Please enter your last name: ")
idnumber = random.randint(0, 100)
idnumber = str(idnumber)

# give the login name
print("Your system login name is ...")

# Get the first letter of the first name
# If the name is 1 character, the slice will return the entire first name of
# 1 character
set1 = first[0:1]

# Get the middle initial
set2 = middle[0:1]

# Get the last initial
set3 = last[0:1]

# Put the sets of characters together
login_name = set1.lower() + set2.lower() + set3.lower() + idnumber

print(login_name)

# Let's create a password checker that meets the following requirements
# It must contain at least 8 characters
# It must contain at least 1 lowercase letter
# It must contain at least 1 uppercase letter
# It must contain at least 1 number

correct_length = False
check_uppercase = False
check_lowercase = False
check_number = False
is_valid = False

print("Please enter your password:")
print("It must contain at least 8 characters")
print("It must contain at least 1 lowercase letter")
print("It must contain at least 1 uppercase letter")
print("It must contain at least 1 number")
password = input()

# Checking for a valid password
while is_valid == False:
    # Check the length
    if len(password) >= 8:
        correct_length = True
        print("Your password has 8 characters.")
    else:
        correct_length = False
        print("Your password does not have 8 characters")
    
    if correct_length:
        print("The password is valid")
        is_valid = True
    else:
        print("The password is invalid")
        is_valid = False
        
        # re-enter the password
        print("Please enter your password:")
        print("It must contain at least 8 characters")
        print("It must contain at least 1 lowercase letter")
        print("It must contain at least 1 uppercase letter")
        print("It must contain at least 1 number")
        password = input()