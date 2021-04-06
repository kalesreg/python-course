# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 12:09:07 2021
account_test.py
@author: kales
"""
# This program demonstrates the BankAccount class

import bankaccount

def main():
    # Get the starting balance
    start_bal = float(input("Enter your starting balance. \n"))
    
    # Get the customer name
    name = input("Enter your name:\n")
    
    # Create a BankAccount object
    savings = bankaccount.BankAccount(start_bal)
    
    # Deposit to the user's paycheck
    pay = float(input("How much were you paid this week?\n"))
    print("I will deposit", format(pay, '.2f'), end = " into your account.")
    savings.deposit(pay)
    
    # Display the balance
    print("\nYour account balance is", format(savings.get_balance(), ',.2f'))
    
    # Get the amount to withdraw
    cash = float(input("How much would you like to withdraw?\n"))
    print("I will withdraw", format(cash, ",.2f"), end = " from your account.")
    savings.withdraw(cash)
    
    # Display the balance
    print("\nYour account balance is", format(savings.get_balance(), ',.2f'))

# Call the main function
main()