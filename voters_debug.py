#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 01:38:26 2019

@author: sherrivaseashta

/**
   This program demonstrates an array of Integer objects.
   It should print out the years and the number of voters each year in Virginia.
   It should print out the year with the most voters
   This is what should display when the program runs as it should
   2017 had  2,612,309 voters.
   2016 had  3,984,631 voters.
   2015 had  1,509,864 voters.
   2014 had  2,194,346 voters.
   2013 had  2,253,418 voters.
   Highest voters is 3,984,631 voters.

"""

def main():
      years = [ 2017, 2016, 2015, 2014, 2013]

      voters = [ 2612309, 3984631, 1509864, 2194346, 2253418]
      
      # I took out highest, highestyear, and sum since they were unused.

      for i in range(len(years)):
      
         print(years[i], " had ", format(voters[i], ",d"), " voters.\n") 
         # Compact print f codes do not allow for ',d' so I changed it to the 
         # print format codes. Alternatively could have ignored the commas or
         # converted them to floats and used ',.0f'
     
      getHighest(years, voters)
      
def getHighest(years, voters):     
      highest = voters[0]
      
      for i in range(len(voters)):
      
         if voters[i] >= highest:
         
         	highest = voters[i] 
      
      print("Highest Voters is ", format(highest, ',d'), " voters.")
      # Same as note above
    

# call the main function
main()
