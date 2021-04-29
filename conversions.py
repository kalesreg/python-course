# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 21:00:19 2021
conversions.py
@author: kales
"""
# Define class Conversions that is used to convert ounces to grams for 
# 3 different measurements of ounces

class Conversions:
    def __init__(self, ounces):
        self.__ounces = ounces
    
    def set_ounces(self, ounces):
        self.__ounces = ounces
    
    def get_ounces(self):
        return self.__ounces
    
"""
# Testing
test = Conversions(8)
print(test.get_ounces())
test.set_ounces(10)
print(test.get_ounces())
"""