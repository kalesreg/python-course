# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 11:47:55 2021
inventory_demo.py
@author: kales
"""
# Test Inventory class

import inventory

def main():
    # Create 3 instances of Inventory object
    item1 = inventory.Inventory("Water", 5, 4.99)
    item2 = inventory.Inventory("Toilet Paper", 1, 5.99)
    item3 = inventory.Inventory("Paper Towels", 3, 11.99)
    
    # Display information
    print("Retail Item 1: ")
    print(item1)
    print("Retail Item 2: ")
    print(item2)
    print("Retail Item 3: ")
    print(item3)

# Call the main function
main()
