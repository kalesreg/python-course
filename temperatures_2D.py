# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 12:39:57 2021
temperatures_2D.py
@author: kales
"""
# This program tracks temperatures over a number of days in a two dimensional
# list that contains strings (dates) and floats (lows, highs, average_temps)

num_days = int(input("How many days do you want to track temperatures:\n"))
COLS = 4

temperatures = [[0 for i in range(COLS)] for j in range(num_days)]
sum_average_temps = 0
highest_high_index = 0

# Loop that loads the values into the lists (lows, highs, average_temps, dates)

for i in range(0, num_days, 1):
    temperatures[i][0] = input("Please enter the date: (ex. Nov. 7):\n")
    print("Please enter the low temperature for ", temperatures[i][0], ":", sep="")
    temperatures[i][1] = float(input())
    print("Please enter the high temperature for ", temperatures[i][0], ":", sep="")
    temperatures[i][2] = float(input())
    temperatures[i][3] = (temperatures[i][1] + temperatures[i][2]) / 2

print("%-15s%15s%15s%15s" % ("Dates", "lows", "Highs", "Average Temps"))

# Loop that displays the values stored in the lists
for j in range(0, num_days, 1):
    print("%-15s%15.1f%15.1f%15.1f" % (temperatures[j][0], temperatures[j][1], \
                                       temperatures[j][2], temperatures[j][3]))

# Code to find the lowest low and the date it occurred on
lowest_low = temperatures[0][1]
lowest_low_date = temperatures[0][0]

for k in range(0, num_days, 1):
    if temperatures[k][1] < lowest_low:
        lowest_low = temperatures[k][1]
        lowest_low_date = temperatures[k][0]

print("%-15s%15.1f" % ("Lowest Low", lowest_low))
print("%-15s%15s" % ("Lowest Low Date", lowest_low_date))

# Code to find the highest high and date it occured on
highest_high = temperatures[0][2]

for m in range(0, len(temperatures), 1):
    if temperatures[m][2] > highest_high:
        highest_high_index = m
        highest_high = temperatures[m][2]

highest_high_date = temperatures[highest_high_index][0]

print("%-15s%15.1f" % ("Highest High", temperatures[highest_high_index][2]))
print("%-17s%13s" % ("Highest High Date", highest_high_date))

# Code to find and display average_temps > 65
for n in range(0, len(temperatures), 1):
    if temperatures[n][3] > 65:
        print("The average temperature exceeded 65 on", temperatures[n][0], \
              "with", temperatures[n][3], "recorded.")

# Code to calculate the average of the average_temps
for p in range(0, len(temperatures), 1):
    sum_average_temps = sum_average_temps + temperatures[p][3]

average_average_temps = sum_average_temps / len(temperatures)

print("The average temperature for all temps recorded is",\
      format(average_average_temps, '.1f'), ".")