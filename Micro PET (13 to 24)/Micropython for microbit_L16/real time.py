# Add your Python code here. E.g.
from microbit import *
from time import sleep

while True:
    light = display.read_light_level()
    display.scroll(light)
    sleep(5)
