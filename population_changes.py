# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 11:41:12 2021
population_changes.py
@author: kales
"""
# The program assumes that all population changes are positive. That is, that
# each year the population was larger than the year before

import matplotlib.pyplot as plt
def main():
    # Set variables
    yearly_change = []
    yearly_population = [0.0] * 41
    change = 0.0
    total_change = 0.0
    average_change = 0.0
    greatest_increase = 0.0
    smallest_increase = 0.0
    greatest_year = 0
    smallest_year = 0
    
    # Constant for the base year
    BASE_YEAR = 1950
    
    try:
        # Open the file for reading
        input_file = open('USPopulation.txt', 'r')
        
        # Read all the lines from the file into a list
        yearly_population = input_file.readlines()
        
        # Set year = BASE_YEAR
        year = BASE_YEAR
        
        # Print headings
        print("%10s%20s" % ("Year", "Population"))
        
        # Change all strings that were read in into floats
        # then print the yearly_population list contents
        for i in range(len(yearly_population)):
            yearly_population[i] = float(yearly_population[i])
            print(format(year, '10d'), end = "")
            print(format(yearly_population[i], '20,.0f'))
            year = year + 1
            
        # Calculate the change in population size for each 2 years
        for j in range(1, len(yearly_population)):
            change = yearly_population[j] - yearly_population[j-1]
            yearly_change.append(change)
            
        # Set year = BASE_YEAR
        year = BASE_YEAR
        # Print headings
        print("\n%-18s%20s" % ("Year to Year", "Population Increase"))
        # Change all string that were read in into floats
        # then print the yearly_population list contents
        for k in range(0, len(yearly_change)):
            print(format(year, '5d'), end = "")
            print('  to ', format(year + 1, '5d'), end="")
            print(format(yearly_change[k], '20,.0f'))
            year = year + 1
        
        # Find the greatest increase and smallest increase
        greatest_increase = max(yearly_change)
        smallest_increase = min(yearly_change)
        
        # Find the index of the greatest_increase and smallest_increase
        for m in range(1, len(yearly_change)):
            if yearly_change[m] == greatest_increase:
                greatest_year = m
            
            if yearly_change[m] == smallest_increase:
                smallest_year = m
            
        total_change = float(sum(yearly_change))
        average_change = total_change / len(yearly_change)
        
        print('The average annual change in population', \
              'during the time period is', format(average_change, ',.1f'))
        print('The year with the greatest increase in population was', \
              BASE_YEAR + greatest_year, 'to', BASE_YEAR + greatest_year + 1)
        print('The year with the smallest increase in population was', \
              BASE_YEAR + smallest_year, 'to', BASE_YEAR + smallest_year + 1)
    
    except IOError:
        print('The file could not be found.')
    except IndexError:
        print('There was an indexing error.')
    except Exception as err:
        print('An error occurred. Give the following to the help desk.')
        print(err)

# Call main        
main()