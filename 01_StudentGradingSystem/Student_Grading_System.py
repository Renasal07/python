#-----------------------------------------------------------------------------
# Name:        (Student_Grading_System.py)
# Purpose:     Coding Challenges (print, variables and conditionals)
#
# Author:      Dr.Renas
# Created:     24-Feb-2025
# Updated:     24-Feb-2025
#-----------------------------------------------------------------------------

# This program that asks for a student's score and then provides a grade based on the score.
store = int(input("Please input your score: "))

# if the score is greater than or equal to 90: Print "Grade: A"
if store >= 90:
    print("Grade: A")
# Else if the score is between 80 and 89 (inclusive): Print "Grade: B"
elif 80 <= store <= 89:
    print("Grade: B")
# Else if the score is between 70 and 79 (inclusive): Print "Grade: C"
elif 70 <= store <= 79:
    print("Grade: C")
# Else if the score is between 60 and 69 (inclusive): Print "Grade: D"
elif 60 <= store <= 69:
    print("Grade: D")
# Else (if the score is below 60): Print "Grade: F"
else:
    print("Grade: F")