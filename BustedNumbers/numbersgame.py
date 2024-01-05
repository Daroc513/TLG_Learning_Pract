#!/usr/bin/env python3

"""Numbers guessing game! User has 5 chances to guess a number between 1 and 100!"""
import random

def main():
    num = random.randint(1,100)

    guess = ""
    rounds = 0

    while rounds < 5 and guess != num:
        guess= input("Guess a number between 1 and 100\n>")

        # COOL CODE ALERT: what is the purpose of the next four lines?
        if guess.isdigit():
            guess= int(guess)
        else:
            continue

        if guess > num:
            print("Too high!")
        elif guess < num:
            print("Too low!")
        else:
            print(f"Correct the number is {72}.")    
       
        rounds += 1

main()
