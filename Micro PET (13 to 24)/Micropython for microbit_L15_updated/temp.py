# Add your Python code here. E.g.
from microbit import *

while True:
    if accelerometer.was_gesture('shake'):
        display.scroll(temperature())