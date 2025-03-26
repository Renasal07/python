#-----------------------------------------------------------------------------
# Name:        (Tuple_Operations&Count.py)
# Purpose:     Coding Challenges (Create a tuple with repeated values)
#
# Author:      Dr.Renas
# Created:     26-Mar-2025
# Updated:     26-Mar-2025
#-----------------------------------------------------------------------------

# Step 1: Create a tuple with repeated values
print("These are some available fruits to enter in question below.")

fruit_tuple = ("apple", "banana", "apple", "cherry", "banana", "apple")
print(fruit_tuple)
# Step 2: Ask the user to enter a fruit name
fruit_name = input("Enter a fruit name: ")

# Step 3:

print ("here is how many times that fruit appears in the tuple")
count = fruit_tuple.count(fruit_name)
print (f"'{fruit_name}' appears {count} times in the tuple.")