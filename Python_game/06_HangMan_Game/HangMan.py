#-----------------------------------------------------------------------------
# Name:        (HangMan.py)
# Purpose:     Coding Challenges (creating a game called HangMan)
#
# Author:      Dr.Renas
# Created:     22-April-2025
# Updated:     22-April-2025
#-----------------------------------------------------------------------------

import random  # This is used to pick random words

# Word categories
# We have a list of easy words for the player to guess
words_by_category = {
    "easy": [  # List of easy words
        "cat", "dog", "sun", "book", "fish", "hat", "tree", "milk", "star", "frog",
        "ball", "bird", "duck", "bike", "cake", "snow", "rain", "sand", "jump", "leaf",
        "apple", "house", "chair", "plane", "train", "grape", "mouse", "cloud", "water", "light"
    ],
}

# Hangman drawing stages
# These are pictures of the hangman showing the progress as the player makes wrong guesses
hangman_stages = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    """
]


# Function to choose a random word from the "easy" category
def choose_word(category):
    # Randomly pick a word from the list of words in the category
    return random.choice(words_by_category[category])


# Function to show the word with underscores for unguessed letters
def get_display_word(word, guessed):
    # This shows the word, but if you haven't guessed the letter, it shows an underscore (_)
    return " ".join([letter if letter in guessed else "_" for letter in word])


# Function to print the introduction to the game
def print_intro():
    print("\n🎮 Welcome to HANGMAN!")
    print("Guess the word before the hangman is fully drawn.")
    print("You only have 6 wrong guesses. Good luck!\n")


# Function to get the user's input
def get_user_choice(prompt, choices):
    while True:
        # Ask the user for input
        choice = input(prompt).lower()
        if choice in choices:
            return choice
        print(f"❗ Invalid choice. Please choose from: {', '.join(choices)}")


# Function to play the actual game
def play_game():
    print_intro()  # Print the welcome message

    category = "easy"  # Set the category to "easy" for this game

    # Get a random word from the "easy" category
    word = choose_word(category)

    # A set to store the letters that the player has guessed
    guessed_letters = set()

    # Start with 0 wrong guesses
    wrong_guesses = 0
    max_wrong = len(hangman_stages) - 1  # Max wrong guesses before game ends

    # Tell the player the category and start the game
    print(f"\n🗂️ Category: Easy | Difficulty: Easy")
    print("-" * 40)

    # Keep playing the game until the player guesses the word or makes too many wrong guesses
    while wrong_guesses < max_wrong:
        # Show the hangman drawing based on how many wrong guesses
        print(hangman_stages[wrong_guesses])

        # Show the current state of the word, with blanks for unguessed letters
        print("Word: ", get_display_word(word, guessed_letters))

        # Show the letters that the player has already guessed
        print("Guessed letters:", " ".join(sorted(guessed_letters)))

        # Ask the player to guess a letter
        guess = input("🔤 Enter a letter: ").lower()

        # Check if the input is a valid letter
        if not guess.isalpha() or len(guess) != 1:
            print("🚫 Please enter a single valid letter.")
            continue

        # Check if the player already guessed this letter
        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
            continue

        # Add the guessed letter to the list of guessed letters
        guessed_letters.add(guess)

        # Check if the guessed letter is in the word
        if guess in word:
            print("✅ Good guess!")
            # If all the letters in the word are guessed, the player wins
            if all(letter in guessed_letters for letter in word):
                print("\n🎉 You won! The word was:", word)
                break
        else:
            print("❌ Wrong guess.")
            # Increase the number of wrong guesses
            wrong_guesses += 1

        # Print a separator line for neatness
        print("-" * 40)

    # If the player runs out of guesses, they lose
    else:
        print(hangman_stages[wrong_guesses])
        print("💀 Game over! The word was:", word)


# Function to let the player play again or quit
def main():
    while True:
        play_game()  # Start a new game
        # Ask the player if they want to play again
        again = input("\n🔁 Do you want to play again? (y/n): ").lower()
        if again != "y":  # If the player doesn't want to play again, end the game
            print("\n👋 Thanks for playing! See you next time!")
            break


# This is the main starting point of the game
if __name__ == "__main__":
    main()  # Run the main game loop
