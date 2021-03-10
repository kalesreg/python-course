# -*- coding: utf-8 -*-
"""
half_me_debug.py
Created on Wed Mar  3 15:26:15 2021
This program should display the following output when debugged
Sum: 1
Sum: 3
Sum: 6
Sum: 10
Sum: 15
Sum: 21
Sum: 28
Sum: 36
Sum: 45
Sum: 55
Halved: 27.5
@author: Kaley Regner
"""

my_sum = 0
halved = 0

for x in range(1, 11): 
    my_sum = my_sum + x
    print("Sum: ", my_sum)

halved = my_sum / 2
print("Halved:", halved)