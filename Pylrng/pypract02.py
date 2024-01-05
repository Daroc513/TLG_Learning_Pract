#!/usr/bin/env python3

#Fancy string work

greet = "Hellp World"

extened_grt = "Hello World," + "This is a long strinig"

name = "DaRoc"

greet_format = "Hello {}"

intruption = f"Whats up {name}"

formatted = greet_format.format(name)

print( intruption, formatted)

print(formatted.upper())
print(formatted.lower())
print(formatted.replace("Daroc", "Roc"))

