# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 11:43:17 2021
cell_phone_list.py
@author: kales
"""
# This program creates 3 CellPhone objects and stores them in a list

import cellphone

def main():
    # Get a list of CellPhone objects
    phones = make_list()
    
    # Display the data in the list
    print("Here is the data that you entered:")
    display_list(phones)
    
# The make_list function gets data from the user for 3 phones. The function 
# returns a list of CellPhone objects containing the data.
def make_list():
    phone_list = []
    
    # Add 3 cell phone objects to the list
    print("Enter data for 3 phones:")
    for count in range(1, 4):
        # Get the phone data
        print("Phone Number " + str(count) + ": ")
        man = input("Enter the manufacturer: ")
        mod = input("Enter the model number: ")
        retail = float(input("Enter the reatil price: "))
        print()
        
        # Create a new CellPhone object in memory and assign to phone variable
        phone = cellphone.CellPhone(man, mod, retail)
        
        # Add the phone to the list
        phone_list.append(phone)
    
    # Return the list
    return phone_list

# The display_list function accepts a list containing CellPhone objects as an 
# argument and displays the data stored in each object
def display_list(phone_list):
    for item in phone_list:
        print("%-20s%20s" % ("Manufacturer:", item.get_manufact()))
        print("%-20s%20s" % ("Model:",item.get_model()))
        print("%-20s%20.2f" % ("Price:",item.get_retail_price()))
        print()
        
# Call the main function
main()
