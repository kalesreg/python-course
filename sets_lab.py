# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 21:46:27 2021
sets_lab.py
@author: kales
"""

# Intersection (What is common in both sets)
setx = set(["green", "blue"])
print(setx)
sety = set(["blue", "yellow"])
print(sety)
setz = setx & sety
print(setz)

# Union
seta = setx | sety
print(seta)

# Add an element to the set
seta.add("red")
print(seta)

# Difference between 2 sets. The values not common in both sets
setb = seta - sety
print(setb)

setc = seta.difference(setx)
print(setc)