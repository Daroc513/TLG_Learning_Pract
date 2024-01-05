#!/usr/bin/env python3

for i in range(99, 0, -1):
    if i > 1:
        print(f"{i} Bottles of beer on the wall, {i} bottles of beer.")
        print(f" Take one down and pass it around, {i -1} bottles of beer on the wall.")

    else:
        print("1 Bottle of beer on the wall, 1 bottle of beer")
        print("Take it down pass it around, no more bottles of beer on the wall")
        print("\nNo more bottles of beer on the wall")
        print("Go to the beer and store some more buy *drunk burp*")
