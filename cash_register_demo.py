# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 12:09:11 2021
cash_register_demo.py
@author: kales
"""
# Test the inventory and cash_register.py classes

import inventory
import cash_register

# Constants to hold the options of purchased items
WINE = 1
PAPER_TOWELS = 2
TOILET_PAPER = 3
BABY_WIPES = 4
WATER = 5

# Main method
def main():
    # Create sale items
    wine = inventory.Inventory('Wine', 20, 12.99)
    paper_towels = inventory.Inventory('Paper Towels', 3, 11.99)
    toilet_paper = inventory.Inventory('Toilet Paper', 1, 5.99)
    baby_wipes = inventory.Inventory('Baby Wipes', 5, 6.59)
    water = inventory.Inventory('Water', 5, 4.99)
    
    # Create a dictionary of sale items
    sale_items = {WINE:wine, PAPER_TOWELS:paper_towels, \
                  TOILET_PAPER:toilet_paper, BABY_WIPES:baby_wipes, \
                  WATER:water}
    
    # Create a cash register object
    register = cash_register.CashRegister()
    
    # Initialize a loop test
    checkout = 'N'
    
    # User wants to purchase items
    while checkout.upper() == 'N':
        user_choice = get_user_choice()
        if user_choice == 1:
            print("Age and/or COVID restrictions may apply.")
        item = sale_items[user_choice]
        if item.get_in_stock() == 0:
            print("The item is out of stock.")
        else:
            register.purchase_item(item)
            
            # Update the time
            new_item = inventory.Inventory(item.get_description(), \
                                           item.get_in_stock(), \
                                           item.get_price())
            
            sale_items[user_choice] = new_item
            
            checkout = input("Are you ready to check out (Y/N)? ")
    
    print()
    print("Your purchase total is", \
          format(register.get_total(), '.2f'))
    print()
    register.show_items()
    register.clear()

def get_user_choice():
    print("Menu")
    print("_____________________________")
    print("1. Wine")
    print("2. Paper Towels")
    print("3. Toilet Paper")
    print("4. Baby Wipes")
    print("5. Water")
    print()
    
    print("Please enter the menu number of the item you would like to puchase:")
    choice = int(input())
    
    while choice < WINE or choice > WATER:
        choice = int(input("Please enter a valid choice from 1 to 5.\n"))
    
    return choice

# Call the main function
main()
            
