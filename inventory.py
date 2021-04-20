# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 11:26:02 2021
inventory.py
@author: kales
"""
# Thise inventory class haleps us to track inventory

class Inventory:
    # Default constructor/method to initialize our attributes/data members
    def __init__(self, description, in_stock, price):
        self.__description = description
        self.__in_stock = in_stock
        self.__price = price
    
    def set_description(self, description):
        self.__description = description
        
    def set_in_stock(self, in_stock):
        self.__in_stock = in_stock
    
    def set_price(self, price):
        self.__price = price
        
    def update_inventory(self):
        self.__in_stock = self.__in_stock - 1
    
    def get_description(self):
        return self.__description 
    
    def get_in_stock(self):
        return self.__in_stock
    
    def get_price(self):
        return self.__price
    
    def __str__(self):
        result = 'Description: ' + self.get_description() + '\n' \
                'Units in stock: ' + str(self.get_in_stock()) + '\n' + \
                'Price: ' + str(self.get_price())
        return result

"""                
# Testing Area
inventory1 = Inventory("water", 2, 1.50)
print("Inventory1", str(inventory1))
print("inventory1", inventory1.__str__())
print("inventory1 description", inventory1.get_description())
"""