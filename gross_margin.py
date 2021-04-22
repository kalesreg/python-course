# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 02:07:55 2021
gross_margin.py
@author: kales
"""

# accepts the user's input from the gm_gui.py file and computes the gross
# margin in $ and gross margin % and displays it

class GrossMargin:
    # Create GrossMargin object
    # should have an __init__ method that accepts the cost and sale form the 
    # gm_gui.py file and initializes the cost and sale
    # Should have a __str__ method that includes decision structures
    # First, if cost and sale enteredby the user is 0 for each, then return 
    # message that says "Nothing from nothing leaves nothing. Try again."
    # If the cost entered by the user is o, then return a message that says
    # "Our suppliers never give us stuff for free. Please re-enter."
    # If the sale entered by the user is 0, then return a message that says
    # "We don't sell stuff for free. Please re-enter."
    # If the user enters a value greater than 0 for the cost and greater 
    # than 0 for the sale, then caluclate the gross_profit_margin by 
    # subtracting the cost from the sale
    # Then calculate the gross_profit_percent by taking the gross_profit_margin
    # and dividing by the sale and then multiplying by 100
    # A string named display_profit will return the following items back to the
    # gross_margin_gui file when tested:
        # Cost in $:   cost
        # Sale in S:   sale
        # Gross Margin in $   gross_profit_margin
        # Gross Margin %   gross_profit_percent