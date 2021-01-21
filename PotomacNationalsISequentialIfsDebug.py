"""
Created on Sun Oct 20 22:11:20 2019

@author: sherrivaseashta
"""
name = input("Please enter your name")
age = int(input("Please enter your age"))
if age >= 18:
    print("Are you an active member of the military or a veteran ", \
          "(Enter Y for Yes, N for No):")
else:
    print("Is your parent an active member of the military or a veteran ", \
         "(Enter Y for Yes, N for No):")
military_status = input()
military_status = military_status.upper()
print("Please choose your seat from the menu below:")
print("FB for Field Box ($17)")
print("BX for Box ($15)")
print("RS for Reserved Seating ($14 for adults, Youth(4-10)/Senior(62+) $13)")
print("GS for Grandstand ($12 for adults, Youth(6-12)/Senior(62+) $11", \
     "Kids 5-and-under Free!)")
seat_type = input()
seat_type = seat_type.upper()
if seat_type == "FB" and age > 5:
    seat_description = "Field Box"
    ticket_price_before_discount = 17
if seat_type == "FB" and age <= 5:
    seat_description = "Field Box"
    ticket_price_before_discount = 0

if seat_type == "BX" and age > 5:
    seat_description = "Box"
    ticket_price_before_discount = 15
if seat_type == "BX" and age <= 5:
   seat_description = "Box"
   ticket_price_before_discount = 0

if seat_type == "RS" and (age >= 4 and age <= 10):
   seat_description = "Reserved Seating"
   ticket_price_before_discount = 13
if seat_type == "RS" and age >= 62:
   seat_description = "Reserved Seating"
   ticket_price_before_discount = 13
if seat_type == "RS" and age < 4:
   seat_description = "Reserved Seating"
   ticket_price_before_discount = 0
if seat_type == "RS" and (age >= 11 and age <=61):
   seat_description = "Reserved Seating"
   ticket_price_before_discount = 14

if seat_type == "GS" and (age >= 6 and age <= 12):
    seat_description = "Grandstand"
    ticket_price_before_discount = 11
if seat_type == "GS" and age >= 62:
   seat_description = "Grandstand"
   ticket_price_before_discount = 11
if seat_type == "GS" and age < 6:
   seat_description = "Grandstand"
   ticket_price_before_discount = 0
if seat_type == "GS" and (age >= 13 and age <= 61):
   seat_description = "Grandstand"
   ticket_price_before_discount = 12

if military_status == "Y":
    military_discount_amount = ticket_price_before_discount * .30
else:
    military_discount_amount = 0

ticket_price_after_discount = ticket_price_before_discount - military_discount_amount

print("Ticket Price for ", name)
print("Age: ", format(age, 'd'))
print("Seat Chosen:", seat_description)
print("Ticket Price Before Discount: ", \
      format(ticket_price_before_discount, ',.2f'))
print("Military Discount: ", format(military_discount_amount, ',d'))
print("Ticket Price After Discount: ", \
      format(ticket_price_after_discount, ',.2f'))

print("Go NATS!!")
