# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 17:18:40 2021
bank_account.py
@author: kales
"""
# Computes and displays the balance based on user input

class BankAccount(object):
    # Accepts balance, deposit, and withdrawal from account_test_gui
    def __init__(self, balance, deposit, withdrawal):
        self._balance = balance
        self._deposit = deposit
        self._withdrawal = withdrawal
    
    def __str__(self):
        # Compute customer_balance
        customer_balance = self._balance
        customer_balance = customer_balance + self._deposit
        
        # Determine if there are sufficient funds
        # Then calculate balance after withdrawal
        if self._withdrawal > customer_balance:
            return 'Insufficient funds: Re-enter withdrawal.'
        else:
            customer_balance = customer_balance - self._withdrawal
        
        # display_balance to return customer_balance with heading
        display_balance = '%20s%10.2f\n' % ('Balance', customer_balance)
        return display_balance
    
