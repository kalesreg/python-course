# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 12:34:07 2021
multi_dimensional_list.py
@author: kales
"""
# Initializing a 2 dimensional list and filling it with random values

import random

# Constants for ROWS and COLD
ROWS = 3
COLS = 4

def main():
    # Create a 2 dimensional list with 3 rows and 4 columns
    values = [[0, 0, 0, 0], 
              [0, 0, 0, 0],
              [0, 0, 0, 0]]
    
    # Fill the list with random numbers
    for r in range(ROWS):
        for c in range(COLS):
            values[r][c] = random.randint(1, 100)
    
    # Display the random numbers
    print(values)

# Call the main function
main()