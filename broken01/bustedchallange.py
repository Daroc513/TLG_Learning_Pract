#!/usr/bin/env python3

def main():

    words= {1: "great",
            2: "Fabulous",
            3: "super"}

    while True:
        name= input("What is your name?\n>")
        num= int(input("Pick a number between 1 and 3: "))

        # Input saves the returned value as a string
        # Num = "2"

        if name and num in words.keys():
        # If the var name has a value
        #if num is one of the keys in the dict words
            # Hi! Welcome to Day 2 of Python Training!
            print("Hi " + name.capitalize() + "! Have a " + words[num] + " day!")
            break
        else:
            print("Come on, follow directions. Try again.")
            continue
            # The conitnue keyword skips over any remaining code and goes back to
            # The beginning of the while loop!

main()
