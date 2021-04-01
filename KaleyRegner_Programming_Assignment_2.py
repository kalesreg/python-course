# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 19:47:22 2021
KaleyRegner_Programming_Assignment_2.py
@author: kales
"""
# Programming Assignment 2 is divided into 6 tasks

import csv

def main():
    # Set variables
    auto_list = [0.0] * 61
    mpg = 0
    sedan_mpg = []
    highest_mpg = 0
    lowest_mpg = 0
    price = 0.0
    all_price = []
    
    try:
        # Task 1
        # Read the file and create the list
        with open("Automobile_data_ITP150.csv", newline = '') as auto_file:
            auto_reader = csv.reader(auto_file, delimiter = ',')
            auto_list = [row for row in auto_reader]
        # Print the list contents
        print(auto_list)
        # Print the number of rows in the list
        print("\nNumber of rows in the list:", len(auto_list))
        
        # Task 2
        # Convert strings to integers
        for i in range(len(auto_list)):
            auto_list[i][2] = int(auto_list[i][2])
            auto_list[i][3] = float(auto_list[i][3])
            
        # Print data types for row 0
        print("\nData type type of row 0, col 0 -->", type(auto_list[0][0]))
        print("Data type type of row 0, col 1 -->", type(auto_list[0][1]))
        print("Data type type of row 0, col 2 -->", type(auto_list[0][2]))
        print("Data type type of row 0, col 3 -->", type(auto_list[0][3]))
                
       # Task 3
        # Print all rows with the headings Manufacturer, Body-Style, MPG, and Price
        print("\n%-20s%15s%10s%20s" % ("Manufacturer", "Body-Style", "MPG", "Price"))
        for j in range(len(auto_list)):    
            print("%-20s%15s%10d%20.2f" % (auto_list[j][0], auto_list[j][1], \
                                           auto_list[j][2], auto_list[j][3]))
        
        # Find the mpg for sedans
        for k in range(len(auto_list)):
            if auto_list[k][1] == "sedan":
                mpg = auto_list[k][2]
                sedan_mpg.append(mpg)
        
        # Display highest mpg for sedans
        highest_mpg = max(sedan_mpg)
        print("\n%-20s%20.1f" % ("Sedan Highest MPG", highest_mpg))
        
        # Find and display lowest mpg for sedans
        lowest_mpg = min(sedan_mpg)
        print("%-20s%20.1f" % ("Sedan Lowest MPG", lowest_mpg))
        
        # Task 4
        # Use a loop to display BMW and Mercedes-Benz cars with prices < 30000
        print("\n%-20s%15s%10s%20s" % ("Manufacturer", "Body-Style", "MPG", "Price"))
        for l in range(len(auto_list)):
            if auto_list[l][0] in ("bmw", "mercedes-benz"):
                if auto_list[l][3] < 30000:
                    price = auto_list[l][3]
                    all_price.append(price)
                    print("%-20s%15s%10d%20.2f" % (auto_list[l][0], \
                        auto_list[l][1], auto_list[l][2], auto_list[l][3]))
        
        # Display count the number of rows BMW and Mercedes-Benz cars with prices < 30000
        print("\n%-35s%20.0f" % ("BMW and MB < 30K Count", len(all_price)))
        
        # Calculate the average price for BMW and Mercedes-Benz cars with prices < 30000
        avg_price = sum(all_price) / len(all_price)
        print("%-35s%20.2f" % ("BMW and MB Avg Price < 30K Count", avg_price))
        
        # Task 5
        # Create an ouput file (CarStatistics.txt) to save results from Task 3 and 4
        stat_file = open('CarStatistics.txt', 'w') # Chose w instead of a, but could have appended but not relevant here
        stat_file.write(str(highest_mpg) + '\n')
        stat_file.write(str(lowest_mpg) + '\n')
        stat_file.write(str(avg_price) + '\n')
        stat_file.close()
        print("Data written to CarStatistics.txt")
    
    # Task 6
    # Use exception handling to alert if file could not be loaded,
    # if a list index error occurred, and if any other error occurred
    except IOError:
        print('The file could not be found.')
    except IndexError:
        print('There was an indexing error.')
    except Exception as err:
        print('An error occurred. Give the following to the help desk.')
        print(err)

# Call the main function
main()