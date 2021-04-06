# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 12:19:06 2021
cellphone.py
@author: kales
"""
# The CellPhone class holds data about a cell phone

class CellPhone:
    # The __init__ method initializes the attributes
    def __init__(self, manufact, model, price):
        self.__manufact = manufact
        self.__model = model
        self.__retail_price = price
    
    # The set_manufact method accepts an argument for the phone;s manufacturer.
    def set_manufact(self, manufact):
        self.__manufact = manufact
    
    # The set_model method accepts an argument for the phone's model
    def set_model(self, model):
        self.__model = model
    
    # The set_reatil_price method accepts an argument for the 
    # phone's reatil price
    def set_retail_price(self, price):
        self.__retail_price = price
    
    # The get_manufact method returns the phone's manufacturer
    def get_manufact(self):
        return self.__manufact
    
    # The get_model method returns the phone's model number
    def get_model(self):
        return self.__model
    
    # The get_retail_price method returns the phone's retail price
    def get_retail_price(self):
        return self.__retail_price

"""
# Test area to test my class
c1 = CellPhone("Apple", "iPhone X", 1000)
print("c1 ", c1.__dict__)
"""