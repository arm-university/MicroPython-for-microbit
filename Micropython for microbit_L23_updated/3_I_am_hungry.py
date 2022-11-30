# Add your Python code here. E.g.
from microbit import *
import speech
import time
import random

while True:
    feeding = random.randint(1, 50)
    display.scroll(feeding) #for testing
    sleep(1000)
    if feeding == 2:
        display.show(Image.SAD) #replace with your own image
        speech.say("I am hungry ", pitch=64, speed=67, mouth=128, throat=128)
        sleep(6000)
    elif feeding > 2:
        display.show(Image.HAPPY)
        sleep(1000)
    