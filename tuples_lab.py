# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 20:57:54 2021
tuples_lab.py
@author: kales
"""

# Create a tuple with different data types
tuple1 = ("tuple", False, 3.2, 1)
print(tuple1)

# Unpack a tuple into several different variables
item1, item2, item3, item4 = tuple1
print(item1, item2, item3, item4)

# Take data in a tuple and add to it
tuple2 = (4, 6, 2, 8, 3, 1, 2)
print(tuple2)

tuple2 = tuple2 + (9,)
print(tuple2)

# Add items to a specific index
tuple2 = tuple2[:5] + (15, 20, 25) + tuple2[:5]
print(tuple2)

# Convert the tuple to a list
list1= list(tuple2)
print(list1)

list1.append(30)
print(list1)

tuple2 = tuple(list1)
print(tuple2)

# Count the repeated items in a tuple
count = tuple2.count(8)
print(count)