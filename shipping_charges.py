# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 22:21:08 2021
shipping_charges.py
@author: kales
"""
# This program determines the shipping costs for a freight company. Shipping
# costs are determined based on the package weight:
    # 00-15 Pounds $10.00
    # 16-35 Pounds $35.00
    # 36-75 Pounds $75.00
    # Over 75 Pounds $1.00 per pound

# Ask user how many packages the customer needs to ship
print("How many packages do you need to ship?", end = " ")
num_packages = int(input())

# For each package, get package number and weight
for i in range(num_packages):
    print("\nWhat is the package number?", end = " ")
    package = int(input())
    
    print("What is the package weight?", end = " ")
    weight = float(input())
    while weight < 0:
        print("Invalid shipping weight. Please enter a value > 0.", end = " ")
        weight = float(input())

    # Determine price based on weight
    if weight <= 15.0:
        price = 10.00
    elif weight <= 35.0:
        price = 35.00
    elif weight <= 75.0:
        price = 75.00
    else:
        price = weight

    # Display the package number, weight, and shipping cost for each package
    print("Package Number:", package)
    print("Package Weight:%.1f" % (weight))
    print("Package Price: $%.2f" % (price))
