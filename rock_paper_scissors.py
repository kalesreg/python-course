# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 11:24:49 2021
rock_paper_scissors.py
@author: kales
"""
# Program that allows you to play Rock, Paper, Scissors using the random number
# generator. 

import random

# Use sentinel value loop to control the program
print("Please enter Play if you want to play the game or anything else to stop.")
run_program = input()
game_counter = 1
ties = 0
user_wins = 0
opponent_wins = 0
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
            print("You chose:", weapon.upper()) # Display the input
        else:
            valid = False
            print("Invalid entry.")
            print("Choose your weapon: R for Rock, P for Paper, or S for Scissors")
            weapon = input()

    # Generate number using random number generator
    opponent_num = random.randint(0, 2)
    # Assign letter to specific number
    if opponent_num == 0:
        opponent_weapon = "R"
    elif opponent_num == 1:
        opponent_weapon = "P"
    else:
        opponent_weapon = "S"
    # Display weapon chosen
    print("I chose:", opponent_weapon)

    # Determine who won the game and display a message. Keep track of tie 
    # games, how many games the user wins, and how many games I win.
    if weapon.upper() == opponent_weapon:
        print("Tie!")
        ties += 1
    elif weapon.upper() == "P" and opponent_weapon == "S":
        print("Scissors beats paper, a win for me!")
        opponent_wins += 1
    elif weapon.upper() == "S" and opponent_weapon == "R":
        print("Rock beats scissors, a win for me!")
        opponent_wins += 1
    elif weapon.upper() == "R" and opponent_weapon == "P":
        print("Paper beats rock! a win for me!")
        opponent_wins += 1
    elif weapon.upper() == "S" and opponent_weapon == "P":
        print("Scissors beats paper, a win for you!")
        user_wins += 1
    elif weapon.upper() == "R" and opponent_weapon == "S":
        print("Rock beats scissors, a win for you!")
        user_wins += 1
    else:
        print("Paper beats rock! a win for you!")
        user_wins += 1
    
    # Either end or continue the while loop
    print("Please enter Play if you want to play the game again or anything else to Stop.")
    run_program = input()

# After stop the game, display report that shows who won the most games
if ties > 0 or user_wins > 0 or opponent_wins > 0:
    print("%4s%20s" % (" ", "~~~Final Score~~~"))
    print("%-14s%15s" % ("Your Score", "My Score"))
    print("%-14s%15s" % (user_wins, opponent_wins))

    # Congratulate the winner
    if user_wins > opponent_wins:
        outplay = user_wins - opponent_wins
        print("Congratulations! You outplayed me by", outplay, "game(s)!")
    elif opponent_wins > user_wins:
        outplay = opponent_wins - user_wins
        print("You're a great opponent! I beat you by only", outplay, "game(s).")
    else:
        print("We're all tied up with", ties, "game(s) each. Let's play again soon.")