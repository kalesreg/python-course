# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 12:11:31 2021
birthdays.py
@author: kales
"""
# This program uses a dictionary for storing birthdays.

# Global constants for menu choices
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

# main function
def main():
    # Create an empty dictionary
    birthdays = {}
    
    # Initialize a variable for the user's choice
    choice = 0
    while choice != QUIT:
        # Get the user's menu choice
        print("Friends and Their Birthdays")
        print("----------------------------")
        print("1. Look up a birthday")
        print("2. Add a new birthday")
        print("3. Change a birthday")
        print("4. Delete a birthday")
        print("5. Quit the program")
        
        # Get the user's choice
        choice = int(input("Enter your choice: "))
    
        # Validate the choice
        while choice < LOOK_UP or choice > QUIT:
            choice = int(input("Enter a valid choice from 1 to 5"))
    
        # Process the choice
        if choice == LOOK_UP:
            # Get a name to look up
            name = input("Enter a name: ")
        
            # Look it up in the dictionary
            print(birthdays.get(name, "Not found"))
        elif choice == ADD:
            # Get a name and birthday
            name = input("Enter a name: ")
            bday = input("Enter a birthday: ")
        
            # If name does not exist, add it
            if name not in birthdays:
                birthdays[name] = bday
            else:
                print("That entry already exists")
        elif choice == CHANGE:
            # Get a name to loopup
            name = input("Enter a name: ")
        
            if name in birthdays:
                # Get a new birthday
                bday = input("Enter the new birthday: ")
            
                # Update the entry
                birthdays[name] = bday
            else:
                print("That name is not found.")
        elif choice == DELETE:
            # Get a name to look up
            name = input("Enter a name: ")
            
            # If the name is found, delete the entry
            if name in birthdays:
                del birthdays[name]
            else:
                print("That name was not found.")
        else:
            print("Never forget a birthday!")
            break

# Call the main() function
main()