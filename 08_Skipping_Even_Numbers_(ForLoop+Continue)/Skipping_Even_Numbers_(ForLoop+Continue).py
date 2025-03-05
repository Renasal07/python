#-----------------------------------------------------------------------------
# Name:        (Skipping_Even_Numbers.py)
# Purpose:     Coding Challenges (For Loop + Continue)
#
# Author:      Dr.Renas
# Created:     5-Mar-2025
# Updated:     5-Mar-2025
#-----------------------------------------------------------------------------

# Loop through numbers from 1 to 10
for num in range(1, 11):  # 11 is exclusive, so it loops from 1 to 10
    # Check if the number is even
    if num % 2 == 0:
        continue  # Skip this iteration for even numbers
    # Print the number if it is odd
    print(num)
