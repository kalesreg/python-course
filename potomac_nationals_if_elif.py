# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 11:08:39 2021
potomac_national_if_elif
@author: kales
"""

print("The Potomac Nationals Welcome You to the Pfitzner Field.")
print("Let's Play Ball!")

# get user input for name and age
name = input("Please enter your name.\n")
age = int(input("Please enter your age.\n"))

# if structure to determine the prompt for military based on age
if age >= 18:
    print("Are you an active member of the military or a veteran?")
    print("Enter Y for Yes or N for No.")
else:
    print("Is your parent an active member of the military or a veteran?")
    print("Enter Y for Yes or N for No.")
military_status = input()
military_status = military_status.upper()

# get user input for seating type
print("Please choose your seat from the menu below:")
print("FB for Field Box ($17)")
print("BX for Box ($15)")
print("RS for Researved Seating ($14 for adults and $13 for " \
      "Youth(4-10)/Senior(62+)")
print("GS for Grandstand ($12 for Adults and $11 for " \
      "Youth(6-12)/Senior(62+). Kids 5-and-under Free!")
seat_type = input()
seat_type = seat_type.upper()

# if structure to determine ticket_price_before_discount
if seat_type == "FB":
    seat_description = "Field Box"
    if age > 5:
        ticket_price_before_discount = 17
    else:
        ticket_price_before_discount = 0
elif seat_type == "BX":
    seat_description = "Box"
    if age > 5:
        ticket_price_before_discount = 15
    else:
        ticket_price_before_discount = 0
elif seat_type == "RS":
    seat_description = "Researved Seating"
    if (age >= 4 and age <= 10) or age >= 62:
        ticket_price_before_discount = 13
    elif age < 4:
        ticket_price_before_discount = 0
    else: 
        ticket_price_before_discount = 14
elif seat_type == "GS":
    seat_description = "Grandstand"
    if (age >= 6 and age <= 12) or age >= 62:
        ticket_price_before_discount = 11
    elif age < 6:
        ticket_price_before_discount = 0
    else:
        ticket_price_before_discount = 12
else:
    seat_description = "Invalid Seat Type. Please run the program."
    ticket_price_before_discount = 0

# compute military discount
if military_status == "Y":
    military_discount_amount = ticket_price_before_discount * 0.30
else:
    military_discount_amount = 0

ticket_price_after_discount = ticket_price_before_discount - \
    military_discount_amount

# display results
print("Ticket Price for", name)
print("Age:", format(age, ',d')) # d means age is an integer
print("Seat Chosen:", seat_description)
print("Ticket Price Before Discount:", \
      format(ticket_price_before_discount, ',.2f'))
print("Military Discount:", format(military_discount_amount, ',.2f'))
print("Ticket Price After Discount:", format(ticket_price_after_discount, ',.2f'))

print("GO NATS!")