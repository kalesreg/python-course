# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 11:52:12 2021
sentinel_value_loop.py
@author: kales
"""

# This program calculates the sum of a series of numbers entered by the user
# and lets the user choose whether or not they want to run the program

grand_total = 0
run_program = input("Please enter Yes to run the program or No to quit")
while run_program.lower() == "yes":
    max_number = 5 # The maximum number
    
    # Initialize the total
    total = 0.0
    
    print("This program calculates the sum of ")
    print(max_number, "numbers that you will enter")
    
    # get the numbers and accumulate sum
    for counter in range(0, max_number, 1):
        number = int(input("Enter a whole number:"))
        total = total + number
        
        print("counter is at", counter)
    
    # display the total of the numbers
    print("The total for just this set of numbers is", total)
    grand_total = grand_total + total
    
    run_program = input("Please enter Yes to run the program again or No to quit")

print("The grand total for each set of numbers run in this program is", \
    grand_total)