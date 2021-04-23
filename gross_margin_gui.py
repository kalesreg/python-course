# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 01:54:35 2021
gross_margin_gui.py
@author: kales
"""

import tkinter
import gross_margin

# Create a class called gm_gui that is a subclass of the Frame class
class gm_gui(tkinter.Frame):
    # Create method that sets up the window and widgets
    def __init__(self):
        # Create the main window
        # Make it automatically run when the window is created
        tkinter.Frame.__init__(self)
        
        # Title should be We <3 $$$ Co.
        self.master.title('We <3 $$$ Co.')
        
        # Set up the grid so that we can arrange the widgets in a 2D table
        self.grid()
        
        # 1st label display "Cost in $:" 
        self.first_label = tkinter.Label(self, text = 'Cost in $: ', justify = 'left', anchor = 'w')
        # 1st label displayed left aligned first row, first column
        self.first_label.grid(sticky = 'w', row = 0, column = 0)
        
        # Cost variable is a double
        self.cost = tkinter.DoubleVar()
        self.cost_entry = tkinter.Entry(self, textvariable = self.cost)
        # Entry widget for the cost should be first row, second column
        self.cost_entry.grid(row = 0, column = 1)

        # 2nd label display "Sale in $:" 
        self.second_label = tkinter.Label(self, text = 'Sale in $: ', justify = 'left', anchor = 'w')
        # 2nd label should be in left aligned second row, first column
        self.second_label.grid(sticky = 'w', row = 1, column = 0)
        
        # Sale variable is a double
        self.sale = tkinter.DoubleVar()
        self.sale_entry = tkinter.Entry(self, textvariable = self.sale)
        #entry widget for sale should be second row, second column
        self.sale_entry.grid(row = 1, column = 1)
        
        # Command button widget will state "Calculate Gross Profit $ and %", when user
        # clicks on it, it should run the compute_gross_profit method
        self.calculate_button = tkinter.Button(self, \
                                        text = 'Calculate Gross Profit $ and %', \
                                        command = self.compute_gross_profit)
        
        # Button should be in the fifth row, first column
        self.calculate_button.grid(row = 4, column = 0, columnspan = 2)
        
        # Output Text widget should be 50 characters wide and 10 lines in height
        self.output = tkinter.Text(self, width = 50, height = 10)
        
        # Output will appear in the sixth row, first column
        self.output.grid(row = 5, column = 0, columnspan = 2)
        
    # compute_gross_profit method will first delete any text in the output Text
    # widget and then use a variable called display_profit as a string to take
    # all output for the GrossMargin object.
    # Insert contents saved in display_profit string variable into the output
    # Text widget.
    def compute_gross_profit(self):
        self.output.delete('1.0', 'end')
        self.gm = gross_margin.GrossMargin(self.cost.get(), self.sale.get())
        self.display_profit = str(self.gm.__str__())
        self.output.insert('1.0', self.display_profit)
        
# Create a method for main() that creates an instance of the gm_gui and runs
# the mainloop() method that waits on the event which is the user clicking 
# the Calculate Gross Profit $ and % command button
def main():
    gm_gui().mainloop()

main()
