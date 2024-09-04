# Add your Python code here. E.g.
from microbit import *
import speech
import time
import random

while True:
    hungry = False
    feeding = random.randint(1, 4) #change after testing
    display.scroll(feeding) #for testing
    sleep(1000)
    if feeding == 2:
        hungry = True
        while hungry is True:
            display.show(Image.SAD) #replace with your own image
            speech.say("I am hungry ", pitch=64, speed=67, mouth=128, throat=128)
            sleep(1000)
            if button_a.is_pressed(): #keep pressing button a to feed the PET
                display.show(Image.HAPPY)
                speech.say("Thank you for my food ", pitch=64, speed=67, mouth=128, throat=128)
                sleep(1000)
                speech.say("You are my friend ", pitch=72, speed=67, mouth=135, throat=128)
                hungry = False
    elif feeding > 2:
        display.show(Image.HAPPY)
        sleep(1000)
    