#!/usr/bin/env python3

#Scope and indentation

RUN_INDENTED = True

message = "running unindented"

if RUN_INDENTED:
    message = "running indented"

print(message)

def my_function():
    greet = "Hello"
    return greet
        
print(my_function())
