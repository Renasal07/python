#-----------------------------------------------------------------------------
# Name:        (Tuple_Operations&Count.py)
# Purpose:     Coding Challenges (Create a tuple with repeated values)
#
# Author:      Dr.Renas
# Created:     26-Mar-2025
# Updated:     26-Mar-2025
#-----------------------------------------------------------------------------

# Step 1: Create a tuple with repeated values
fruit_tuple = ("apple", "banana", "apple", "cherry", "banana", "apple")

# Step 2: Ask the user to enter a fruit name
fruit_name = input("Enter a fruit name: ")

# Step 3:

print ("here is how many times that fruit appears in the tuple")
count = fruit_tuple.count(fruit_name)
print (f"'{fruit_name}' appears {count} times in the tuple.")