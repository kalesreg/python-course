# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 11:56:30 2021
cash_register.py
@author: kales
"""
# Shows how inheritance works by inheriting from inventory

import inventory

class CashRegister:
    # Initialize a list to hold purchased items
    def __init__(self):
        self.__items = []
        
    # Method to clear the contents of the cash register
    def clear(self):
        self.__items = []
    
    # Method that simulates adding an item to the cash register
    # Receives an Inventory object as an argument
    def purchase_item(self, inventory_item):
        self.__items.append(inventory_item)
        print("The item was added to the cash register.")
        inventory_item.update_inventory()
    
    # Method to return the total cost of items at the cash register 
    def get_total(self):
        total = 0.0
        for item in self.__items:
            total = total + item.get_price()
        
        return total
    
    # Method that prints a list of items at the cash register
    def show_items(self):
        print("The items in the cash register are ")
        print()
        for item in self.__items:
            print(item)
            print()
       
