# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 11:57:03 2021
population_changes_EC.py
@author: kales
"""
# The program assumes that all population changes are positive. That is, that
# each year the population was larger than the year before

import matplotlib.pyplot as plt
def main():
    # Set variables
    yearly_change = []
    population_list = [0.0] * 41
    change = 0.0
    total_change = 0.0
    average_change = 0.0
    greatest_increase = 0.0
    smallest_increase = 0.0
    greatest_year = 0
    smallest_year = 0
    
    # Constant for the base year
    BASE_YEAR = 1950
    import csv
    
    try:
        # Open the file for reading
        with open("USPopulationEC.txt", newline = '') as population_file:
            population_reader = csv.reader(population_file, delimiter = '\t')
            population_list = [row for row in population_reader]
        print(population_list)
        
        # Read all the lines from the file into a list
        print("Number of rows in the list:", len(population_list))
        
        # Print headings
        print("%10s%20s" % ("Year", "Population"))
        
        # Change all strings that were read in into floats
        # then print the population_list list contents
        for i in range(len(population_list)):
            population_list[i][0] = int(population_list[i][0])
            population_list[i][1] = float(population_list[i][1])
            print(format(population_list[i][0], '10d'), end = "")
            print(format(population_list[i][1], '20,.0f'))
           
        # Calculate the change in population size for each 2 years
        for j in range(1, len(population_list)):
            change = population_list[j][1] - population_list[j-1][1]
            yearly_change.append(change)
          
        # Set year = BASE_YEAR
        year = BASE_YEAR
        # Print headings
        print("\n%3s%-18s%20s" % (" ", "Year to Year", "Population Increase"))
        # Change all string that were read in into floats
        # then print the population_list list contents
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
        
        # Create a list containing the week numbers (to use as an axis in a chart)
        years_list = []
        for y in range(1950, 1991, 1):
            years_list.append(y)
        
        # Plot the population increases between 1950 and 1959
        for n in range(len(yearly_change)):
            if years_list[n] >= 1950 and years_list[n] <= 1959:
                plt.bar(years_list[n], yearly_change[n])
                # Add a title
                plt.title("Population Increases Betweeen 1950 and 1959")
                # Add labels to the axes
                plt.xlabel('(1950-1959)')
                plt.ylabel('Population Increase in Millions')
        plt.show()
        
    except IOError:
        print('The file could not be found.')
    except IndexError:
        print('There was an indexing error.')
    except Exception as err:
        print('An error occurred. Give the following to the help desk.')
        print(err)

# Call main        
main()
