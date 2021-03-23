# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 11:25:01 2021
add_coffee_record.py
@author: kales
"""
# This program adds coffee inventory records to a coffee.txt file

def main():
    # Create a variable to control the loop
    another = 'y'
    
    try:
        # Open the coffee.txt file in append mode
        coffee_file = open('coffee.txt', 'a')
        
        # Add records to the file
        while another.lower() == "y":
            # Get the coffee record data
            print("Enter the following coffee data:")
            descr = input("Description: ")
            qty = int(input("Quantity (in pounds): "))
            
            # Append the data to the file
            coffee_file.write(descr + '\n')
            coffee_file.write(str(qty) + '\n')
            
            # Determine whether the user wants to add another record to the file
            print("Do you want to add another record?")
            another = input("y for yes, anything else is no: ")
            
        # Close the file
        coffee_file.close()
        print("Data appended to coffee.txt")
        
    except IOError:
        print("An error occurred trying to read the file")
    
    except:
        print("An error occurred")

# Call the main function
main()
