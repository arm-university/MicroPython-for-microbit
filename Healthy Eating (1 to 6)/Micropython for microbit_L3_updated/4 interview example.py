# Add your Python code here. E.g.
from microbit import *

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        display.scroll("Yes")
    elif button_b.is_pressed():
        display.show(Image.SAD)
    elif button_a.is_pressed():
        display.show(Image.GHOST)
    else:
        display.show(Image.ASLEEP)

display.clear()
