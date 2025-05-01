import pygame
import random
import sys

# Initialize Pygame and mixer
pygame.init()
pygame.mixer.init()

# Load background music
pygame.mixer.music.load("chill-beats.mp3")  # Replace with your .mp3 file name
pygame.mixer.music.set_volume(0.4)  # Volume (0.0 to 1.0)
pygame.mixer.music.play(-1)  # Loop indefinitely

# Load sound effects
wrong_guess_sound = pygame.mixer.Sound("wrong-sound.mp3")  # Replace with the actual sound file
win_sound = pygame.mixer.Sound("goodresult.mp3")  # Replace with the actual sound file
lose_sound = pygame.mixer.Sound("losing-horn.mp3")  # Replace with the actual sound file

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

words = [
    "doctor", "teacher", "engineer", "nurse", "pilot", "chef", "artist", "lawyer", "soldier", "plumber",
    "carpenter", "scientist", "astronaut", "musician", "actor", "farmer", "mechanic", "dancer", "writer", "photographer"
]
word = random.choice(words).upper()
guessed = []
hangman_status = 0
MAX_WRONG = 6


# Draw the hangman using Pygame primitives
def draw_hangman(stage):
    base_x = 50
    base_y = 300
    pole_height = 120
    arm_length = 60
    head_radius = 12

    # Base
    pygame.draw.line(win, BLACK, (base_x, base_y), (base_x + 60, base_y), 3)  # bottom
    pygame.draw.line(win, BLACK, (base_x + 30, base_y), (base_x + 30, base_y - pole_height), 3)  # pole
    pygame.draw.line(win, BLACK, (base_x + 30, base_y - pole_height), (base_x + 30 + arm_length, base_y - pole_height),
                     3)  # top bar
    pygame.draw.line(win, BLACK, (base_x + 30 + arm_length, base_y - pole_height),
                     (base_x + 30 + arm_length, base_y - pole_height + 20), 3)  # rope

    if stage > 0:
        pygame.draw.circle(win, BLACK, (base_x + 30 + arm_length, base_y - pole_height + 35), head_radius, 2)  # head
    if stage > 1:
        pygame.draw.line(win, BLACK, (base_x + 30 + arm_length, base_y - pole_height + 47),
                         (base_x + 30 + arm_length, base_y - pole_height + 90), 2)  # body
    if stage > 2:
        pygame.draw.line(win, BLACK, (base_x + 30 + arm_length, base_y - pole_height + 55),
                         (base_x + 30 + arm_length - 20, base_y - pole_height + 70), 2)  # left arm
    if stage > 3:
        pygame.draw.line(win, BLACK, (base_x + 30 + arm_length, base_y - pole_height + 55),
                         (base_x + 30 + arm_length + 20, base_y - pole_height + 70), 2)  # right arm
    if stage > 4:
        pygame.draw.line(win, BLACK, (base_x + 30 + arm_length, base_y - pole_height + 90),
                         (base_x + 30 + arm_length - 20, base_y - pole_height + 110), 2)  # left leg
    if stage > 5:
        pygame.draw.line(win, BLACK, (base_x + 30 + arm_length, base_y - pole_height + 90),
                         (base_x + 30 + arm_length + 20, base_y - pole_height + 110), 2)  # right leg


# Display text when game ends
def display_message(text, sound_effect):
    pygame.time.delay(1000)
    win.fill(WHITE)
    message = WORD_FONT.render(text, True, BLACK)
    win.blit(message, (WIDTH / 2 - message.get_width() / 2, HEIGHT / 2))
    pygame.display.update()

    # Play the sound for win or lose
    sound_effect.play()

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
    win.blit(word_text, (WIDTH / 2 - word_text.get_width() / 2, 200))

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
                        wrong_guess_sound.play()  # Play wrong guess sound

    won = all(letter in guessed for letter in word)
    if won:
        display_message("You Won!", win_sound)  # Play win sound
        break

    if hangman_status >= MAX_WRONG:
        display_message(f"You Lost! Word was: {word}", lose_sound)  # Play lose sound
        break
