#-----------------------------------------------------------------------------
# Name:        (Guess_the_Number.py)
# Purpose:     Coding Challenges (While Loop, Import, and if statements)
#
# Author:      Dr.Renas
# Created:     4-Mar-2025
# Updated:     4-Mar-2025
#-----------------------------------------------------------------------------

import random
print(" Please guess a number between 1 and 10.")
# Step 1: Generate a random number between 1 and 10
random_number = random.randint(1, 10)

# Step 2: Start the while loop
while True:
    # Prompt the user to guess the number
    guess = int(input("Guess the number: "))  # Convert input to an integer

    if guess == random_number:  # Check if the guess is correct
        print("Correct! 🎉")  # If correct, print success message
        break  # Exit the loop
    else:
        print("Wrong, try again!")  # If incorrect, give feedback and continue
