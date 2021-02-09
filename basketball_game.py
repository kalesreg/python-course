# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 11:22:54 2021
basketball_game.py
@author: kales
"""

import random

player1_name = input("Please enter the player 1 name:")
player2_name = input("Please enter the player 2 name:")

counter = 0
player1_score = 0
player2_score = 0
for i in range(1, 5, 1):
    print("****************************** QUARTER", i, \
          "******************************")
    print("%-16s%-23s%-30s\n" % (" ", player1_name, player2_name))
    print("%-10s%-12s%-12s%-12s%-12s\n" % ("Shot#", "Shot", "Score", "Shot", "Score"))
    for shot in range(30, 721, 30):
        player1_shots = random.randint(0, 3)
        counter = counter + 1
        if player1_shots == 0:
            player1_shotmade = "Air Ball"
        elif player1_shots == 1:
            player1_shotmade = "Free Throw"
        elif player1_shots == 2:
            player1_shotmade = "Two Points"
        else:
            player1_shotmade = "3 Pointer"
        player1_score = player1_score + player1_shots
        
        player2_shots = random.randint(0, 3)
        if player2_shots == 0:
            player2_shotmade = "Air Ball"
        elif player2_shots == 1:
            player2_shotmade = "Free Throw"
        elif player2_shots == 2:
            player2_shotmade = "Two Points"
        else:
            player2_shotmade = "3 Pointer"
        player2_score = player2_score + player2_shots
        
        print("%-10s%-12s%-12s%-12s%-12s\n" % (counter, player1_shotmade, \
            player1_score, player2_shotmade, player2_score))

print("-----------------------------------------------------------")

if player1_score > player2_score:
    print(player1_name, "bringing a W!")
elif player2_score > player1_score:
    print(player2_name, "bringing a W!")
else:
    print("Tie Game.")