#!/usr/bin/env python3
"""RZFeeser | Alta3 Research
   learning about for logic"""

# create the list called vendors
vendors = ["cisco", "juniper", "big_ip", "f5", "arista"]
# create a second list of strings
approved_vendors = ["cisco", "juniper", "big_ip"]
# loop across the list vendors
for x in vendors:
    print("\nThe vendor is " + x, end="") # A newline, print current vendor, and end without newline
    if x not in approved_vendors: # if x does not appear with the list approved_vendors
        print(" - NOT AN APPROVED VENDOR!", end="")
print("\nOur loop has ended.")  # when the loop ends print this

