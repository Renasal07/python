#-----------------------------------------------------------------------------
# Name:        (Skipping_Even_Numbers.py)
# Purpose:     Coding Challenges (For Loop + Continue)
#
# Author:      Dr.Renas
# Created:     5-Mar-2025
# Updated:     5-Mar-2025
#-----------------------------------------------------------------------------

# Loop through numbers from 1 to 10
# Ask the user for the upper limit
upper_limit = int(input("Enter the upper limit (1 to ?): "))

# Loop through numbers from 1 to the user-specified upper limit
for num in range(1, upper_limit + 1):  # Adding 1 because the stop value in range is exclusive

    if num % 2 == 0:
        continue  # Skip this iteration for even numbers
    # Print the number if it is odd
    print(num)

print("Hey did you know that I skipped all the even numbers?")