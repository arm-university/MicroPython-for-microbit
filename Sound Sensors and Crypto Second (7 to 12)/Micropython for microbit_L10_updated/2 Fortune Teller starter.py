# Add your Python code here. E.g.
from microbit import *
import random

answers = [
    "Yes",
    "No",
    "I cannot answer that yet"
    ]

while True:
    display.show("?")
    if accelerometer.was_gesture("shake"):
        display.clear()
        sleep(1000)
        display.scroll(random.choice(answers))
