#-----------------------------------------------------------------------------
# Name:        ( Tuple_Basics.py)
# Purpose:     Coding Challenges (Create a tuple with five different elements,
#              including an integer, a float, a string, a boolean, and another tuple.)
#
# Author:      Dr.Renas
# Created:     25-Mar-2025
# Updated:     25-Mar-2025
#-----------------------------------------------------------------------------

# Create a tuple with five different elements
my_tuple = (42, 3.14, 'Python', True, (1, 2, 3))

# 1. Print the entire tuple
print("Entire tuple:", my_tuple)

# 2. Access and print the third element (index 2)
third_element = my_tuple[2]
print("Third element (index 2):", third_element)

# 3. Extract the nested tuple and print its first element
nested_tuple = my_tuple[4]
first_element_of_nested_tuple = nested_tuple[0]
print("First element of the nested tuple:", first_element_of_nested_tuple)