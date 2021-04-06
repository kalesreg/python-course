# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 12:44:40 2021
cell_phone_test.py
@author: kales
"""
# This program test the CellPhone class

import cellphone

def main():
    # Get the phone data
    man = input("Enter the manufacturer: ")
    mod = input("Enter the model number: ")
    retail = float(input("Enter the retail price: "))
    
    # Create an instance of the CellPhone class
    phone = cellphone.CellPhone(man, mod, retail)
    
    # Display the data that was entered
    print("Here is the data that you entered:")
    print("Manufacturer: ", phone.get_manufact())
    print("Model: ", phone.get_model())
    print("Retail Price: $", format(phone.get_retail_price(), ',.2f'), sep = '')

# Call the main function
main()
