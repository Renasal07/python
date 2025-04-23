import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game")

# Fonts and Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 50)
LETTER_FONT = pygame.font.SysFont('comicsans', 30)

# Game variables
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 450
A = 65

for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])

words = ["cat", "dog", "fish", "book", "hat", "snow", "apple", "cloud"]
word = random.choice(words).upper()
guessed = []
hangman_status = 0
MAX_WRONG = 6

# Draw the hangman using Pygame primitives
def draw_hangman(stage):
    # Base
    pygame.draw.line(win, BLACK, (150, 500), (450, 500), 5)  # bottom
    pygame.draw.line(win, BLACK, (300, 500), (300, 100), 5)  # pole
    pygame.draw.line(win, BLACK, (300, 100), (450, 100), 5)  # top bar
    pygame.draw.line(win, BLACK, (450, 100), (450, 150), 5)  # rope

    if stage > 0:
        pygame.draw.circle(win, BLACK, (450, 180), 30, 3)  # head
    if stage > 1:
        pygame.draw.line(win, BLACK, (450, 210), (450, 300), 3)  # body
    if stage > 2:
        pygame.draw.line(win, BLACK, (450, 230), (400, 270), 3)  # left arm
    if stage > 3:
        pygame.draw.line(win, BLACK, (450, 230), (500, 270), 3)  # right arm
    if stage > 4:
        pygame.draw.line(win, BLACK, (450, 300), (400, 350), 3)  # left leg
    if stage > 5:
        pygame.draw.line(win, BLACK, (450, 300), (500, 350), 3)  # right leg

# Display text when game ends
def display_message(text):
    pygame.time.delay(1000)
    win.fill(WHITE)
    message = WORD_FONT.render(text, True, BLACK)
    win.blit(message, (WIDTH / 2 - message.get_width() / 2, HEIGHT / 2))
    pygame.display.update()
    pygame.time.delay(3000)

# Draw the game screen
def draw():
    win.fill(WHITE)

    # Title
    text = FONT.render("Hangman", True, BLACK)
    win.blit(text, (WIDTH / 2 - text.get_width() / 2, 20))

    # Word display
    display_word = ""
    for letter in word:
        display_word += letter + " " if letter in guessed else "_ "
    word_text = WORD_FONT.render(display_word, True, BLACK)
    win.blit(word_text, (400 - word_text.get_width() / 2, 200))

    # Letters
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, True, BLACK)
            win.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))

    # Draw hangman
    draw_hangman(hangman_status)

    pygame.display.update()


# Game loop
run = True
while run:
    draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr, visible = letter
                if visible and ((x - mx) ** 2 + (y - my) ** 2) ** 0.5 < RADIUS:
                    letter[3] = False
                    guessed.append(ltr)
                    if ltr not in word:
                        hangman_status += 1

    won = all(letter in guessed for letter in word)
    if won:
        display_message("🎉 You Won!")
        break

    if hangman_status >= MAX_WRONG:
        display_message(f"💀 You Lost! Word was: {word}")
        break
