#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 01:38:26 2019

@author: sherrivaseashta

/**
   This program demonstrates an array of String objects.
   It should print out the days and the number of hours spent at work each day.
   It should print out the day of the week with the most hours worked
   It should print out the average number of hours worked each day 
   This is what should display when the program runs as it should
   Sunday has 12 hours worked.
   Monday has 9 hours worked.
   Tuesday has 8 hours worked.
   Wednesday has 13 hours worked.
   Thursday has 6 hours worked.
   Friday has 4 hours worked.
   Saturday has 0 hours worked.
   Highest Day is Wednesday with 13 hours worked
   Average hours worked in the week is 7.43 hours
"""

def main():
      days = [ "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

      hours = [ 12, 9, 8, 13, 6, 4, 0] # Error: Saturday hours missing

      average = 0.0
      highest = 0
      highestDay = " "
      sum = 0

      for i in range(len(days)):
      
         print(days[i], " has ", hours[i], " hours worked.") # Error: Fixed commas, index to i
      
     
      highest = hours[0]

      for i in range(len(days)):
      
         if hours[i] >= highest: # Error: if statement syntax, index to i
         
         	highest = hours[i] # Error: index to i
         	highestDay = days[i] # Rrror: days not hours, index to i
         
         sum = sum + hours[i] # Error: index to i
      
      average = sum / 7 # Error: division flipped
      print("Highest Day is ", highestDay, " with ", highest, " hours worked")
      print("Average hours worked in the week is %4.2f hours" % (average))

# call the main function
main()