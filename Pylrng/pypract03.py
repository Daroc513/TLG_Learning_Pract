#!/usr/bin/env python3

#Gettin what I need from lists with slices

NAMES= ["DaRoc", "Nicki", "Wayne", "Drake"]
AGES = [20, 21, 22, 23]

DAROC = NAMES[0]
NICKI = NAMES[1]

DAROC_NICKI = NAMES[:2]
WAYNE_DRAKE = NAMES[2:]
REVERSE = NAMES[::-1]
EVERY_OTHER = NAMES[::2]

print(sum(AGES))
print(min(AGES))
print(min(AGES))

print(DAROC_NICKI)
print(WAYNE_DRAKE)
print(REVERSE)
