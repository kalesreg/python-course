# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 12:43:17 2021
unpickle_cellphone.py
@author: kales
"""
# This program unpickles CellPhone objects

import pickle
import cellphone

# Constant for filename
FILENAME = 'cellphone.dat'

def main():
    # To indicate the end of file
    end_of_file = False
    
    # Open a file
    input_file = open(FILENAME, 'rb')
    
    # Get the data from the user
    while not end_of_file:
        try:
            # Unpickle the next object
            phone = pickle.load(input_file)
            
            # Display the cell phone data
            display_data(phone)
            
        except EOFError:
            # Set the flag to indicate the end of file has been reached
            end_of_file = True
    
    # Close the file
    input_file.close()
    
# The display_data function displays data from the CellPone object passed
# as an argument
def display_data(phone):
    print("%-20s%20s" % ("Manufacturer:", phone.get_manufact()))
    print("%-20s%20s" % ("Model:", phone.get_model()))
    print("%-20s%20.2f" % ("Price:",phone.get_retail_price()))
    print()

# Call the main function
main()