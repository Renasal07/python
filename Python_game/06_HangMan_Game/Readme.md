readme_content = """
# Hangman Game: Python Edition

Welcome to the **Hangman Game: Python Edition**! This is a simple, fun word-guessing game where you try to guess the hidden word by suggesting letters. But be careful—if you make too many wrong guesses, the hangman is drawn, and you lose the game!

## Game Rules

1. You will be given a word with missing letters.
2. You will guess one letter at a time.
3. If you guess a letter that is in the word, it will be revealed in its correct position.
4. If you guess a wrong letter, a part of the hangman figure will be drawn.
5. You can make **6 wrong guesses** before the game is over.
6. The game ends when either:
   - You guess all the letters correctly (you win!).
   - Or you make 6 wrong guesses (you lose!).

## How to Play

1. The game will start by giving you a random word to guess.
2. It will show blanks (`_`) for each letter in the word, and you will guess one letter at a time.
3. If you guess a letter correctly, it will appear in the word.
4. If you guess a letter incorrectly, the hangman figure will be drawn bit by bit.
5. You have **6 chances** to make a wrong guess before the hangman is fully drawn.
6. After the game ends, you can choose to play again.

## Features

- Random word selection from an easy word list.
- Interactive gameplay where you guess one letter at a time.
- ASCII art that shows the hangman figure progressively.
- Option to play again after finishing a game.

## Requirements

To play this game, you will need:
- **Python 3.x** installed on your system.

## How to Run the Game

1. Download or clone this repository to your computer.
2. Open your terminal or command prompt.
3. Navigate to the folder where the game file is located.
4. Run the game by typing the following command:

   ```bash
   python hangman_game.py
