# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 02:07:55 2021
gross_margin.py
@author: kales
"""
# Accepts the user's input from the gm_gui.py file and computes the gross
# margin in $ and gross margin % and displays it

# Create GrossMargin object
class GrossMargin:
    # should have an __init__ method that accepts the cost and sale form the 
    # gm_gui.py file and initializes the cost and sale
    def __init__(self, cost, sale):
        self.__cost = float(cost)
        self.__sale = float(sale)
    
    # Should have a __str__ method that includes decision structures
    def __str__(self):
        # First, if cost and sale entered by the user is 0 for each, then return 
        # message that says "Nothing from nothing leaves nothing. Try again."
        if self.__cost == 0 and self.__sale == 0:
            return "Nothing from nothing leaves nothing. Try again."
        # If the cost entered by the user is 0, then return a message that says
        # "Our suppliers never give us stuff for free. Please re-enter."
        elif self.__cost == 0:
            return "Our suppliers never give us stuff for free. Please re-enter."
        # If the sale entered by the user is 0, then return a message that says
        # "We don't sell stuff for free. Please re-enter."
        elif self.__sale == 0:
            return "We don't sell stuff for free. Please re-enter."
        # If the user enters a value greater than 0 for the cost and greater 
        # than 0 for the sale, then caluclate the gross_profit_margin by 
        # subtracting the cost from the sale. Then calculate the 
        # gross_profit_percent by taking the gross_profit_margin
        # and dividing by the sale and then multiplying by 100
        else:
            if self.__cost > 0 and self.__sale > 0:
                gross_profit_margin = self.__sale - self.__cost
                gross_profit_percent = gross_profit_margin / self.__sale * 100
            
            # A string named display_profit will return the following items back to the
            # gross_margin_gui file when tested:
            # Cost in $:   cost
            # Sale in S:   sale
            # Gross Margin in $   gross_profit_margin
            # "Gross Margin %"   gross_profit_percent
            display_profit = '%-20s%10.2f' % ('Cost in $:', self.__cost)
            display_profit += '\n%-20s%10.2f' % ('Sale in S:', self.__sale)
            display_profit += '\n%-20s%10.2f' % ('Gross Margin in $', gross_profit_margin)
            display_profit += '\n%-20s%10.2f' % ('Gross Margin %', gross_profit_percent)
        
            return display_profit

"""
# Testing area
test = GrossMargin(100, 200)
print(test.__str__())
"""
