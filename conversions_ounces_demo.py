# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 21:07:51 2021
conversion_ounces_demo.py
@author: kales
"""
# Program that uses the Conversions class

from conversions import Conversions

def main():
    my_ounces = make_list()
    
    print('Here are the measurements that you entered')
    display_list(my_ounces)
    
    display_totals(my_ounces)

def make_list():
    ounces_list = []
    
    for i in range(3):
        print('Please enter the ounces for Item', (i+1), end='')
        user_input = float(input())
        ounces_object = Conversions(user_input)
        ounces_list.append(ounces_object)
        print()
    
    return ounces_list

def display_list(ounces_list):
    print('%-10s%-10s' % ('Ounces', 'Grams'))
    for j in ounces_list:
        print('%-10.1f%-10.1f' % (j.get_ounces(), (j.get_ounces() * 28.35)))
        
def display_totals(ounces_list):
    ounces_total = 0.0
    for k in ounces_list:
        ounces_total = ounces_total + k.get_ounces()
    grams_total = ounces_total * 28.35
    
    print('---------------------------')
    print('%-10.1f%-10.1f' % (ounces_total, grams_total))
    print('===========================')

main()
