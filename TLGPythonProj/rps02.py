#!/usr/bin/env python3
#FreeCodeCamp Youtube Tutorial chapter 8: Loops
#Infinite ROCK, PAPER, SCISSORS!

# value = input('Please enter a value:\n')
# print(value)
import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    #Adding a loop to play over and over.
playagain =True

while playagain:
    
    playerchoice = input(
        "\nROCK, PAPER, SCISSORS SHOOT!...\n1. Rock 🪨 \n2. Paper 📄 \n3. Scissors ✂️:\n\n")

    player = int(playerchoice)

    if player < 1 or player > 3:
        print("You must enter 1, 2, or 3.")
        continue

    computerchoice = random.choice("123")

    computer = int(computerchoice)

    print("\nYou chose " + playerchoice + ".")
    print("Python chose " + computerchoice + ".\n")

    if player == 1 and computer == 3:
        print("You win!😁")
    elif player == 2 and computer == 1:
        print("You win! 😁")
    elif player == 3 and computer == 2:
        print("You win!😁")
    elif player == computer:
        print("Tie game!🤯")
    else:
        print("Python wins!🐍")

        playagain = input("\n\nRun it back?\n Y for yes or \n Q to Quit \n\n")

        if playagain.lower() == "q":
            print("\n🎉🎉🎉🎉")
            print("Hope you had as much fun as I did, thanks for playing!\n")
            playagain = False #Or use break
