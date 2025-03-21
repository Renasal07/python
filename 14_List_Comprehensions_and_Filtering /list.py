#-----------------------------------------------------------------------------
# Name:        (list.py)
# Purpose:     Coding Challenges (create a list)
#
# Author:      Dr.Renas
# Created:     21-Mar-2025
# Updated:     21-Mar-2025
#-----------------------------------------------------------------------------

# Create a list of numbers from 1 to 10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Create a list of even numbers using a list comprehension
even_numbers = [num for num in numbers if num % 2 == 0]

# Create a list of squares of the even numbers
squared_numbers = [num ** 2 for num in even_numbers]

# Print the resulting lists
print(even_numbers)
print(squared_numbers)
