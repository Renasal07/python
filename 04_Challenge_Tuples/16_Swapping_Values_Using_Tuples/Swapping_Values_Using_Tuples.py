#-----------------------------------------------------------------------------
# Name:        (Swapping_Values_Using_Tuples.py)
# Purpose:     Coding Challenges (swapping values easily using tuples)
#
# Author:      Dr.Renas
# Created:     25-Mar-2025
# Updated:     25-Mar-2025
#-----------------------------------------------------------------------------

# Step 1: Ask the user to input two numbers
first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))

# Step 2: Store the numbers in a tuple
numbers_tuple = (first_number, second_number)
print(f"Original values: {numbers_tuple}")
# Step 3: Swap the values using tuple
swapped_tuple = (numbers_tuple[1], numbers_tuple[0])

# Step 4: Print the swapped values
print(f"Swapped values: {swapped_tuple}")