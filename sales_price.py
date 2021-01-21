# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 11:55:34 2021
sales_price.py
@author: kales
"""

# This program gets an item's original price and
# calculates its sale price, with a 20% discount

# Get the item's original price
original_price = float(input("Enter the item's original price:"))

# Calculate the amount of the discount
discount = original_price * 0.20

# Calculate sale price
sale_price = original_price - discount

# Display the sale price
print("The sale price is", sale_price)