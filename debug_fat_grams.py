#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 23:25:57 2019

@author: sherrivaseashta
"""

"""
   This program demonstrates a solution to the
   Fat Gram Calculator programming challenge.
   fatCalories = fatGrams * 9
   fatPercentage = fatCalories / calories
   When debugged, calories of 100 and fat grams of 10 should
   display percentage of calories from fat is 90.0%
"""


   
calories = 0.0        # Number of calories
fat_grams = 0.0        # Number of fat grams
fat_calories = 0.0     # Calories from fat
fat_percentage = 0.0   # Percentage of fat calories

#Get the number of calories.
print("How many calories does the food have? ")
calories = float(input())
      
#Get the number of fat grams.
fat_grams = float(input("How many fat grams does the food have? "))

#calculate the fatCalorie
fat_calories = fat_grams * 9
      
#Calculate percentage of calories from fat.
fat_percentage = fat_calories / calories
      
#display the results
print("The percentage of calories from fat is %.1f%s" % (fat_percentage * 100, "%."))
