# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 11:39:54 2021
discounts.py
@author: kales
"""
# This program will calculate the discount for early payments of a utility bill.

print("Utility Bill Early Payment Calculator")
# Input for the number of customers
print("How many customers are you processing today?", end = "")
num = int(input())

for i in range(1, num + 1):
    # Input for customer's name, amount paid, and how many days the payment was
    # received before the original due date.
    print("\nPlease enter the customer's last name:", end = "")
    name = input()
    print("Please enter the amount paid:", end = "")
    paid = float(input())
    print("By how many days was the payment made in advance?", end = "")
    advance = int(input())
    # Validate the days early to make sure not 
    # less than 1 and more than 30 days early
    while advance < 1 or advance > 30:
        print("Invalid Days")
        print ("Days must be between 1 and 30.", end = "")
        advance = int(input())

    # Early discounts:
        # 01-10 days = 1% 
        # 11-20 days = 1.5%
        # 21-30 days = 2%
    if advance <= 10:
        discount_amt = 0.01
    elif advance <= 20:
        discount_amt = 0.015
    else:
        discount_amt = 0.02
    
    # Calculate discount
    discount = paid * discount_amt

    # Display report contiaining customer's name, amount paid, days early, 
    # and discount. 2 decimal places for monetary amounts and in columns.
    print("Here is the information for the discount:")
    print("%-15s%15s" % ("Name", name)) # Long name may cause formatting issues
    print("%-15s%15.2f" % ("Amount Paid", paid))
    print("%-15s%15d" % ("Days Early", advance))
    print("%-15s%15.2f" % ("Discount", discount))
