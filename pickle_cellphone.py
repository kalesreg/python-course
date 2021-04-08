# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 12:31:46 2021
pickle_cellphone.py
@author: kales
"""
# This program pickles (serializes) cell phone objects

import pickle
import cellphone

# Constant for the filename
FILENAME = 'cellphone.dat'

def main():
    # Initalize a variable to contorl the loop
    again = 'y'
    
    # Open a file
    output_file = open(FILENAME, 'wb')
    
    # Get data from the user
    while again.lower() == 'y':
        # Get cell phone data
        man = input("Enter the manufacturer: ")
        mod = input("Enter the model number: ")
        retail = float(input("Enter the reatil price: "))
        
        # Create a cell phone object
        phone = cellphone.CellPhone(man, mod, retail)
        
        # Pickle the CellPhone object
        pickle.dump(phone, output_file)
        
        # Get more cell phone data
        again = input("Enter more phone data? (Y/N): ")
    
    # Close the file
    output_file.close()
    print("The data was written to", FILENAME)

# Call the main function
main()