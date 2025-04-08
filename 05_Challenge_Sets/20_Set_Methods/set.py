#-----------------------------------------------------------------------------
# Name:        (set.py)
# Purpose:     (covers set methods like .copy(), .clear(), and .pop().)
#
# Author:      Dr.Renas
# Created:     2-Apr-2025
# Updated:     2-Apr-2025
#-----------------------------------------------------------------------------


# Create the set
data = {10, 20, 30, 40, 50}

# Copy the set to data_copy
data_copy = data.copy()
print(f"Copy: {data_copy}")

# Pop a random element from the set
data.pop()
print(f"After pop: {data}")

# Clear the set
data.clear()
print(f"After clear: {data}")
