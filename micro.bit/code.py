from microbit import *
import random

display.scroll('321')
# create a random deLay

# create a counter
counter = 0
tries = 0
times = []
# create a go signal and measure how lon it takes to press a button
while tries < 3:
    sleep(random.randint(2000, 3000))
    display.show(Image.BUTTERFLY)
    while True:
        sleep(10)
        counter += 1
        if button_a.is_pressed():
            display.scroll('TIME:' + str(counter))
            times.append(counter)
            counter = 0
            tries += 1
            break

while True:
    if button_a.is_pressed():
        display.scroll('AV:' + str(sum(times) / 3))
    elif button_b.is_pressed():
        display.scroll('BEST:' + str(min(times)))