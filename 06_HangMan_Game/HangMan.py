import random

# Word categories
words_by_category = {
    "easy": [
        "cat", "dog", "sun", "book", "fish", "hat", "tree", "milk", "star", "frog",
        "ball", "bird", "duck", "bike", "cake", "snow", "rain", "sand", "jump", "leaf",
        "apple", "house", "chair", "plane", "train", "grape", "mouse", "cloud", "water", "light"
    ],
}

# Hangman ASCII stages
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