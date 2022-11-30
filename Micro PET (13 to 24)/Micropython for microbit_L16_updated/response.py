# Add your Python code here. E.g.
from microbit import *
from time import sleep

while True:
    light = display.read_light_level()
    if light > 20:
        display.show(Image.HAPPY)
    else:
        display.show(Image.SAD)
