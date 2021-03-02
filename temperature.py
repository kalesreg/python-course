# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 11:35:54 2021
temperature.py
@author: kales
"""
# This program tracks temperatures over a number of days in lists.

num_days = int(input("How many days do you want to track temperatures?\n"))

lows = [0.0] * num_days
highs = [0.0] * num_days
average_temps = [0.0] * num_days
dates = [" "] * num_days
sum_average_temps = 0.0

# Load the values into the lists (lows, highs, average_temps, dates)
for i in range(0, num_days, 1):
    dates[i] = input("Please enter the date: (ex. Nov 7)\n")
    print("Please enter the low temperature for ", dates[i], ":", sep="", end="")
    lows[i] = float(input())
    print("Please enter the high temperature for ", dates[i], ":", sep="", end="")
    highs[i] = float(input())
    average_temps[i] = (lows[i] + highs[i]) / 2

print("%-15s%15s%15s%15s" % ("Dates", "Lows", "Highs", "Average Temps"))
for j in range(num_days):
    print("%-15s%15.1f%15.1F%15.1f" % (dates[j], lows[j], highs[j], \
                                       average_temps[j]))

# Code to find the lowest low and the date it occurred on
lowest_low = lows[0]
lowest_low_date = dates[0]

for k in range(0, len(lows), 1):
    if lows[k] < lowest_low:
        lowest_low = lows[k]
        lowest_low_date = dates[k]
 
print("%-20s%15.1f" % ("Lowest Low", lowest_low))
print("%-20s%15s" % ("Lowest Low Date", lowest_low_date))

# Code to find the highest high and the date it occurred on
highest_high = highs[0]
highest_high_date = dates[0]

for m in range(0, len(lows), 1):
    if highs[m] > highest_high:
        highest_high = highs[m]
        highest_high_date = dates[m]
 
print("%-20s%15.1f" % ("Highest High", highest_high))
print("%-20s%15s" % ("Highest High Date", highest_high_date))

# Code to find the lowest high date by saving the index for lowest high
lowest_high_index = 0
lowest_high = highs[0]

for n in range(len(highs)):
    if highs[n] < lowest_high:
        lowest_high = highs[n]
        lowest_high_index = n
        
print("%-20s%15.1f" % ("Lowest High", lowest_high))
print("%-20s%15s" % ("Lowest High Date", dates[lowest_high_index]))

# Code to find the highest low date by saving the index for highest low
highest_low_index = 0
highest_low = lows[0]

for p in range(len(lows)):
    if lows[p] > highest_low:
        highest_low = lows[p]
        highest_low_index = p
        
print("%-20s%15.1f" % ("Highest Low", highest_low))
print("%-20s%15s" % ("Highest Low Date", dates[highest_low_index]))

# Code to print the days where low temperatures fell below freezing 32F
for q in range(len(lows)):
    if lows[q] < 32:
        print("The low of ", lows[q], " fell below freezing on ", dates[q], ".", sep="")

# Code to calculate the average of the average_temps
for s in range(0, len(average_temps), 1):
    sum_average_temps = sum_average_temps + average_temps[s]
        
average_average_temps = sum_average_temps / len(average_temps)

print("The average temperature for all temps recorded is ",\
      format(average_average_temps, '.1f'), ".", sep="")