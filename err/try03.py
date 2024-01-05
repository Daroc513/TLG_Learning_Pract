#!/usr/bin/env python3
"""Catching specific errors | Atla3 Research"""

# Start with ab infinite loop
while True:
    try:
        print("Let's divide x by y!")
        x = int(input("What is the integer value of x? "))
        y = int(input("What is the integer value of y?"))
        print("The value of x/y:", x / y)
    except ZeroDivisionError as zerr:
        print("Handling run-time error:", zerr)
        # general error handling
        # a practical use might be exceptions we haven't designed solution for yet
    except Exception as err:
        # sys.exc_info returns a 3 tuple with into about the expection handled
        print("We did not anticipate that:", err)
        # raise by itself simply calls the previous exception that was thrown
        raise
    # else ONLY runs if there wasn't any errors
    else:
        print("\nThanks for learning to handle errors!")
        break