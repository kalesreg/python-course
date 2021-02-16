# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 11:24:49 2021
rock_paper_scissors.py
@author: kales
"""
# Program that allows you to play Rock, Paper, Scissors using the random number
# generator. 

# Use sentinel value loop to control the program
print("Please enter Play if you want to play the game or anything else to stop.")
run_program = input()
game_counter = 1
while run_program.upper() == "PLAY":
    print("Game", game_counter, "Rock, Paper, Scissors - Play!")
    game_counter = game_counter + 1 # Count the number of games played
    
    # Provide information for input options and get input
    print("Choose your weapon: R for Rock, P for Paper, or S for Scissors")
    weapon = input()

    # Validate the choice of weapon
    valid = False
    while valid == False:
        if weapon.upper() == "R" or weapon.upper() == "P" or weapon.upper() == "S":
            valid = True
        else:
            valid = False

    # Display the input

    # Generate number using random number generator

    # Assign letter to specific number

    # Display weapon chosen

    # Determine who won the game
    
    # Either end or continue the while loop
    print("Please enter Play if you want to play the game again or anything else to Stop.")
    run_program = input()

# Display a message and keep track of tie games, how many games the user wins,
# and how many games I win.

# After stop the game, display report that shows who won the most games

# Congratulate the winner




# 2/16/2021 11:30-11:35, 11:43-12:10