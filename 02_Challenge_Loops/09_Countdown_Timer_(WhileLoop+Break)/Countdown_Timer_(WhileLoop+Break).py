#-----------------------------------------------------------------------------
# Name:        (Countdown_Timer.py)
# Purpose:     Coding Challenges (While Loop + Break)
#
# Author:      Dr.Renas
# Created:     6-Mar-2025
# Updated:     6-Mar-2025
#-----------------------------------------------------------------------------

# Countdown from 10 to 1
count = 10  # Initialize the countdown variable

while count > 0:  # Continue looping while count is greater than 0
    print(count)  # Print the current countdown number
    count -= 1  # Decrease the countdown variable by 1

    # Prompt the user to stop or continue
    user_input = input('Enter "stop" to cancel or press Enter to continue: ')

    if user_input.lower() == "stop":  # Check if the user entered "stop"
        print("Countdown stopped!")  # Notify the user the countdown has stopped
        break  # Exit/break out of the loop

    # After the loop ends, the program exits