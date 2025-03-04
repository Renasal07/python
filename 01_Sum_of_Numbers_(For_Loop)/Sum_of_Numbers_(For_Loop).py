# Ask the user for a number
num = int(input("Enter a number: "))

# Initialize the variable to store the sum
total_sum = 0

# Iterate through numbers from 1 to n (inclusive)
for i in range(1, num + 1):
    total_sum += i  # Add the current number to the running sum

# Print the final sum
print(f"The sum of all numbers from 1 to {num} is: {total_sum}")