#-----------------------------------------------------------------------------
# Name:        New File Generator (Temperature_Advice.py)
# Purpose:     Coding Challenges (print, variables and conditionals)
#
# Author:      Dr.Renas
# Created:     24-Feb-2025
# Updated:     24-Feb-2025
#-----------------------------------------------------------------------------
temperature = int(input("What is the temperature outside? "))

# If the temperature is below 10°C
if temperature < 10:
    print("It's cold outside. Wear a jacket!")
# elif the temperature is between 10°C and 25°C
elif 10 <= temperature < 25:
    print("It's a nice day. Wear short-sleeves!")
# elif the temperature is between 10°C and 25°C
else:
    print("It's hot outside. Stay cool!")
