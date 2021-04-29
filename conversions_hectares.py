# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 10:31:57 2021
conversions_hectares.py
@author: kales
"""
# Class to get and set hectare measurements

class ConversionsHectares:
    def __init__(self, hectare):
        self.__hectare = hectare
    
    def set_hectare(self, hectare):
        self.__hectare = hectare
    
    def get_hectare(self):
        return self.__hectare
    
"""
# Testing
test = ConversionsHectares(10)
print(test.get_hectare())
test.set_hectare(15)
print(test.get_hectare())
"""


