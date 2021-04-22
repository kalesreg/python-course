# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 01:54:35 2021
gross_margin_gui.py
@author: kales
"""

import tkinter
import gross_margin

# Create a class called gm_gui that is a subclass of the Frame class

# Create method that sets up the window and widgets
# Make it automatically run whe the window is created
# Title should be We <3 $$$ Co.
# Set up the grid so that we can arrange the widgets in a 2D table
# 1st label display "Cost in $:" which should be in first row, first column
# and should be left aligned and stick the W part
# The sale variable is a double, the entry widget for the cost should be 
# first row, second column
# 2nd label display "Sale in $:" and label should be in second row, first column
# Label should be left aligned, stick to W part of the grid
# Sale vairable is a double, entry widget for sale should be second row, second column
# Command button widget will state "Calculate Gross Profit $ and %", when user
# clicks on it, it should run the compute_gross_profit method
# Button should be in the fifth row, first column
# Output Text widget should be 50 characters wide and 10 lines in height
# and will appear in the sixth row, first column
# compute_gross_profit method will first delete any text in the output Text
# widget and then use a variable called display_profit as a string to take
# all output for the GrossMargin object.
# Insert contents saved in display_profit string variable into the output
# Text widget.
# Create a method for main() that creates an instance of the gm_gui and runs
# the mainloop() method that waits on the event which is the user clicking 
# the Calculate Gross Profit $ and % command button
