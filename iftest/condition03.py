#!/user/bin/env python3

hostname = input("what value should we set for hostname?")

## notice how the first line has changed
## here we use the str.lower() method to return a lowercase string

if hostname.lower() =="mtg":
    print("The hostname was found to be mtg")
