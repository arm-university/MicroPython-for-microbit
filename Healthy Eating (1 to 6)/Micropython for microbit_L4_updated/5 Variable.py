# Add your Python code here. E.g.
from microbit import *

total = 0

while True:
    if button_a.is_pressed():
        total = total + 1
        sleep(100)
        display.scroll(total)
    elif button_b.is_pressed():
        total = total - 2
        sleep(100)
        display.show(total)
    elif button_a.is_pressed() and button_b.is_pressed():
        total = 0
        sleep(100)
        display.show(total)
    else:
        display.show(Image.SMILE)
