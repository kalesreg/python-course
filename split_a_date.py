# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 11:21:07 2021
split_a_date.py
@author: kales
"""

# The purpose of this program is to split a date at the / and store the month,
# day, and year separately

# Create a string with a date
date_string = "10/28/2020"

# Split the date
date_list = date_string.split('/')

# Display each piece of the data
print("Month: ", date_list[0])
print("Day: ", date_list[1])
print("Year: ", date_list[2])