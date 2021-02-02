# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 11:25:47 2021
number_guessing_game.py
@author: kales
"""

import random

print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.")
print("You get a maximum of 6 tries.")

# Set the initial volaues
secret_number = random.randint(1, 100)

# Guessing loop
guess = int(input("Take a guess: "))
tries = 1

while guess != secret_number and tries < 6:
    if guess > secret_number:
        print("Lower Please")
    else:
        print("Higher Please")
    
    guess = int(input("Take a guess: "))
    tries = tries + 1

if guess == secret_number:
    print("You guessed it! The number was", secret_number)
    print("And it only took you", tries, "tries!\n")

input("\n\nPress the enter key to exit.")