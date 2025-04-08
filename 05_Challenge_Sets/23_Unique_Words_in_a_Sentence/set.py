#-----------------------------------------------------------------------------
# Name:        (set.py)
# Purpose:     Coding Challenges (Extract unique words, and Split the sentence into words)
#
# Author:      Dr.Renas
# Created:     4-Apr-2025
# Updated:     4-Apr-2025
#-----------------------------------------------------------------------------

sentence = "The quick brown fox jumps over the lazy dog"

# Split the sentence into words
words = sentence.split()

# Convert the list of words into a set to get unique words
unique_words = set(words)

# Print the set of unique words
print(unique_words)