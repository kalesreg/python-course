# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 12:53:30 2021
kilo_converter_gui.py
@author: kales
"""

import tkinter
import tkinter.messagebox

class KiloConverterGUI:
    def __init__(self):
        # Create the main window
        self.main_window = tkinter.Tk()
        
        # Create 3 frames to group widgets
        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()
        
        # Create the widgets for the top frame
        self.prompt_label = tkinter.Label(self.top_frame, \
                                          text = "Enter kilometers:")
        self.kilo_entry = tkinter.Entry(self.top_frame, width = 10)
        
        # Pack the top frame's widgets
        self.prompt_label.pack(side='left')
        self.kilo_entry.pack(side='right')
        
        # Create the widgets for the middle frame
        self.descr_label = tkinter.Label(self.mid_frame, \
                                         text = "Converted to Miles: ")
        
        # Create a StringVar object for the outfield
        self.value = tkinter.StringVar()
        
        # Create a label associated with the StringVar() object
        self.miles_label = tkinter.Label(self.mid_frame, \
                                         textvariable = self.value)
        
        # Pack the middle frame's widgets
        self.descr_label.pack(side = 'left')
        self.miles_label.pack(side = 'left')
            
        # Create the button widgets for the bottom frame
        self.calc_button = tkinter.Button(self.bottom_frame, text = "Convert", \
                                          command = self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text = "Quit", \
                                          command = self.main_window.destroy)
        
        # Pack the buttons
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')
        
        # Pack the frames
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
        
        # Enter the tkinter main loop
        tkinter.mainloop()
    
    # The convert method is a callback function for the Convert button
    def convert(self):
        # Get the value entered by the user into the kilo entry widget
        kilo = float(self.kilo_entry.get())
        
        # Convert to miles
        miles = kilo * 0.6214
        
        # Display the results in the same window
        self.value.set(miles)
        

# Create an instance of the KiloConverterGUI class
kilo_conv = KiloConverterGUI()
        
