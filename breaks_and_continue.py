# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 12:54:20 2021
breaks_and_continue.py
@author: kales
"""

# Use of break statement inside a loop to break out of the loop as soon as the
# letter "i" is encountered

for val in "Daniel":
    if val == "i":
        break
    print(val)

print("The end")

# Use of continue inside a loop to skip past an iteration as soon as 
# "i" is encountered

for val in "Daniel":
    if val == "i":
        continue
    print(val)

print("The end")

# Use of continue to skip printing 74 and 75 when printing 1-100
for x in range(1, 101, 1):
    if x == 74 or x == 75:
        continue
    print(x)

print("The end")