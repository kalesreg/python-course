# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 16:41:39 2021
account_test_gui.py
@author: kales
"""

from tkinter import *
from bank_account import BankAccount

class account_test_gui(Frame):
    def __init__(self):
        # Set up window and widgets
        Frame.__init__(self)
        self.master.title('We <3 You Bank ATM')
        self.grid()
        
        # Label and Input fields
        self._balance_label = Label(self, justify = LEFT, \
                                    text = 'Enter starting balance: ', \
                                    anchor = 'w')
        self._balance_label.grid(sticky = W, row = 0, column = 0)
        self._balance_var = DoubleVar()
        self._balance_entry = Entry(self, textvariable = self._balance_var)
        self._balance_entry.grid(row = 0, column = 1)
        
        self._deposit_label = Label(self, justify = LEFT, \
                                    text = 'Enter deposit: ', \
                                    anchor = 'w')
        self._deposit_label.grid(sticky = W, row = 1, column = 0)
        self._deposit_var = DoubleVar()
        self._deposit_entry = Entry(self, textvariable = self._deposit_var)
        self._deposit_entry.grid(row = 1, column = 1)
        
        self._withdrawal_label = Label(self, justify = LEFT, \
                                       text = 'Enter withdrawal: ', \
                                       anchor = 'w')
        self._withdrawal_label.grid(sticky = W, row = 2, column = 0)
        self._withdrawal_var = DoubleVar()
        self._withdrawal_entry = Entry(self, \
                                       textvariable = self._withdrawal_var)
        self._withdrawal_entry.grid(row = 2, column = 1)
        
        # Command buttons
        self._button = Button(self, text = 'Display Balance', \
                              command = self._compute_balance)
        self._button.grid(row = 3, column = 0, columnspan = 2, \
                          stick = W+E+N+S)
        
        # Output Area
        self._output_area = Text(self, width = 50, height = 10)
        self._output_area.grid(row = 4, column = 0, columnspan = 2, \
                               sticky = W+E+N+S)
    
    # Delete text, compute the balance, and display in the text widget
    def _compute_balance(self):
        self._output_area.delete('1.0', END)
        # Event handler for compute button
        display_balance = str(BankAccount(self._balance_var.get(), \
                                          self._deposit_var.get(), \
                                          self._withdrawal_var.get()))
        self._output_area.insert('1.0', display_balance)

# Create instance and run mainloop()
def main():
    account_test_gui().mainloop()

main()