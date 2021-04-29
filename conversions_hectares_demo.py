# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 10:38:19 2021
conversions_hectares_demo.py
@author: kales
"""
# Convert hectares to acres for 4 different measurements of hectares

from conversions_hectares import ConversionsHectares

def main():
    my_list = make_list()
    
    print('Here are the measurements that you entered:')
    display_list(my_list)
    
    display_totals(my_list)

# Prompts user for input, creates list of hectares, and returns it
def make_list():
    hectares_list = []
    
    for item in range(4):
        print('Please enter the total hectares for Item', (item + 1), end = '')
        user_input = float(input())
        hectares_object = ConversionsHectares(user_input)
        hectares_list.append(hectares_object)
    
    return hectares_list

# Displays list of hectares and converts them to acres
def display_list(hectares):
    print('%-15s%15s' % ('Hectares', 'Acres'))
    for item in hectares:
        print('%-15.0f%15.2f' % (item.get_hectare(), \
                                  (item.get_hectare() * 2.471052)))

# Displays total for hectares and acres
def display_totals(hectares):
    hectares_total = 0.0
    for item in hectares:
        hectares_total = hectares_total + item.get_hectare()
    acres_total = hectares_total * 2.471052
    
    print('-------------------------------')
    print('%-15.1f%15.2f' % (hectares_total, acres_total))
    print('===============================')

main()

