# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 12:03:44 2021
bankaccount.py
@author: kales
"""
# The BankAccount class simulates a bank object

class BankAccount:
    # The __init__ method accepts an argument for the account's balance.
    # It is assigned to the __balance attribute.
    def __init__(self, bal):
        self.__balance = bal
    
    # The deposit method makes a deposit into the account
    def deposit(self, amount):
        self.__balance += amount
    
    # The withdrawn method withdraws an amount from the account
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Error: Insufficient funds")
    
    # The get_balance method returns the account balance
    def get_balance(self):
        return self.__balance

    def __str__(self):
        return "BankAccount Inputs({})".format(self.bal)

"""
Test area to see if the methods work
bank1 = BankAccount(5000)
print("bank1", str(bank1.get_balance()))
"""