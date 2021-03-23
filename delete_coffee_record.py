# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 13:00:28 2021
delete_coffee_record.py
@author: kales
"""
# This program allows the user to delete a record in the coffee.txt file

import os # Needed for the remove and renaming of a file

def main():
    # Create a bool variable to use as a flag
    found = False
    
    try:
        # Get the coffee to delete
        search = input("Which coffee do you want to delete?")
        
        # Open the original coffee.txt file
        coffee_file = open('coffee.txt', 'r')
        
        # Open the temporary file
        temp_file = open('temp.txt', 'w')
        
        # Read the first record's description field
        descr = coffee_file.readline()
        
        # Read the rest of the file
        while descr != '':
            # Read the quantity field
            qty = int(coffee_file.readline())
            
            # Strip the \n from the description
            descr = descr.rstrip('\n')
            
            # If this is not the record to delete, then write it to temp file
            if descr != search:
                # Write the record to the file
                temp_file.write(descr + '\n')
                temp_file.write(str(qty) + '\n')
            else:
                found = True
            
            # Read the next desciption
            descr = coffee_file.readline()
            
        # Close the coffee file and temp file
        coffee_file.close()
        temp_file.close()
        
        # Delete the original coffee.txt file
        os.remove('coffee.txt')
        
        # Rename the temp file
        os.rename('temp.txt', 'coffee.txt')
        
        # If the search value was not found in the file, then display message
        if found:
            print("The file has been updated.")
        else:
            print("That item was not found in the file.")
            
    except IOError:
        print("An error occurred trying to read the file.")
    except:
        print("An error occurred.")

# Call the main function
main()
